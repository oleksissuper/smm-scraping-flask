<script>
import { ref, watch, onMounted, onUnmounted } from "vue";
import { fetchRecords } from "../services/api";

export default {
  props: {
    selectedNetwork: {
      type: String,
      required: true,
    },
    selectedFilter: {
      type: String,
      default: null,
    },
    rateRange: {
      type: Object,
      default: () => ({ from: null, to: null }),
    },
  },
  setup(props) {
    const records = ref([]);
    const isLoading = ref(false);
    const error = ref(null);
    const page = ref(1);
    const limit = 20;
    const expandedRows = ref(new Set());
    const isEndReached = ref(false);

    const columnMappings = {
      service_name: "Service Name",
      rate_per_thousand: "Rate per Thousand",
      minimum_quantity: "Min Quantity",
      maximum_quantity: "Max Quantity",
      average_time: "Average Time",
      category_service: "Category",
      source: "Source",
    };

    const toggleRow = (id) => {
      if (expandedRows.value.has(id)) {
        expandedRows.value.delete(id);
      } else {
        expandedRows.value.add(id);
      }
    };

    const loadRecords = async (reset = false) => {
      if (isLoading.value || isEndReached.value) return;
      isLoading.value = true;
      error.value = null;

      try {
        if (reset) {
          page.value = 1;
          records.value = [];
          isEndReached.value = false;
        }

        const requestData = {
          network: props.selectedNetwork,
          filters: props.selectedFilter ? [props.selectedFilter] : null,
          rate_range: [props.rateRange.from, props.rateRange.to].filter(
            (value) => value !== null
          ),
          page: page.value,
          limit: limit,
        };

        const fetchedRecords = await fetchRecords(requestData);

        if (fetchedRecords.length < limit) {
          isEndReached.value = true;
        } else {
          isEndReached.value = false;
        }

        records.value = [...records.value, ...fetchedRecords];
        page.value += 1;
      } catch (err) {
        error.value = err.message || "Failed to load records";
      } finally {
        isLoading.value = false;
      }
    };

    const handleScroll = () => {
      const scrollHeight = document.documentElement.scrollHeight;
      const scrollTop = document.documentElement.scrollTop;
      const clientHeight = document.documentElement.clientHeight;

      if (scrollTop + clientHeight >= scrollHeight - 100) {
        loadRecords();
      }
    };

    watch(
      () => props.selectedNetwork,
      () => {
        page.value = 1;
        isEndReached.value = false;
        loadRecords(true);
      }
    );

    watch(
      () => props.selectedFilter,
      () => {
        page.value = 1;
        isEndReached.value = false;
        loadRecords(true);
      }
    );

    watch(
      () => props.rateRange,
      (newRange, oldRange) => {
        if (newRange.from !== oldRange.from || newRange.to !== oldRange.to) {
          isEndReached.value = false;
          loadRecords(true);
        }
      },
      { deep: true }
    );

    const handlePageReset = () => {
      loadRecords(true);
    };

    onMounted(() => {
      loadRecords(true);
      window.addEventListener("scroll", handleScroll);
    });

    onUnmounted(() => {
      window.removeEventListener("scroll", handleScroll);
    });

    return {
      records,
      columnMappings,
      isLoading,
      error,
      loadRecords,
      expandedRows,
      toggleRow,
      isEndReached,
      handlePageReset,
    };
  },
};
</script>
<template>
  <div>
    <h2>Records</h2>
    <div class="table-responsive small">
      <table class="table table-striped table-sm">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th
              v-for="(displayName, key) in columnMappings"
              :key="key"
              scope="col"
            >
              {{ displayName }}
            </th>
          </tr>
        </thead>
        <tbody>
          <template
            v-for="(record, index) in records"
            :key="record.id || index"
          >
            <tr
              @click="toggleRow(record.id)"
              :class="{ 'table-secondary': index % 2 === 1 }"
              style="cursor: pointer"
            >
              <td>{{ index + 1 }}</td>
              <td v-for="(displayName, key) in columnMappings" :key="key">
                {{ record[key] }}
              </td>
            </tr>
            <tr
              v-if="expandedRows.has(record.id)"
              :class="{ 'table-light': index % 2 === 1 }"
            >
              <td colspan="100%">
                <strong>Description:</strong>
                <div>{{ record.description }}</div>
              </td>
            </tr>
          </template>
        </tbody>
      </table>
    </div>
    <div v-if="error" class="alert alert-danger mt-3">
      {{ error }}
    </div>
    <div v-if="isLoading" class="text-center mt-3">Loading...</div>
    <div v-if="isEndReached" class="text-center mt-3">No more records.</div>
  </div>
</template>

<style scoped>
.clickable-row {
  cursor: pointer;
}
.table-responsive {
  margin-top: 20px;
}
</style>
