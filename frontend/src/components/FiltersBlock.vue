<template>
  <div>
    <h5>Filters for: {{ selectedNetwork }}</h5>
    <n-space>
      <n-button
        v-for="(filter, index) in filters"
        :key="index"
        quaternary
        :type="filter === selectedFilter ? 'info' : 'default'"
        @click="handleFilterClick(filter)"
      >
        {{ filter }}
      </n-button>
    </n-space>
    <h5>Rate per Thousand:</h5>

    <div class="rate-range mt-3">
      <n-input
        v-model:value="rateRange.from"
        placeholder="From"
        type="number"
        size="small"
        @input="updateRateRange"
      />
      <span class="mx-2">to</span>
      <n-input
        v-model:value="rateRange.to"
        placeholder="To"
        type="number"
        size="small"
        @input="updateRateRange"
      />
    </div>
  </div>
</template>

<script>
import { NButton, NSpace, NInput } from "naive-ui";

export default {
  props: {
    selectedNetwork: {
      type: String,
      required: false,
    },
    filters: {
      type: Array,
      required: true,
    },
    selectedFilter: {
      type: String,
      default: null,
    },
  },
  emits: ["selectFilter", "updateRateRange"],
  components: {
    NButton,
    NSpace,
    NInput,
  },
  data() {
    return {
      rateRange: {
        from: null,
        to: null,
      },
    };
  },
  methods: {
    handleFilterClick(filter) {
      this.$emit("selectFilter", filter);
    },
    updateRateRange() {
      const range = {
        from: this.rateRange.from || null,
        to: this.rateRange.to || null,
      };
      this.$emit("updateRateRange", range);
    },
  },
};
</script>

<style scoped>
.rate-range {
  display: flex;
  align-items: center;
}
.mx-2 {
  margin: 0 8px;
}
.mt-3 {
  margin-top: 16px;
}
</style>
