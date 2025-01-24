<template>
  <div class="container-fluid">
    <div class="row">
      <LeftSide @selectNetwork="handleNetworkSelect" :networks="networks" />
      <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
        <div
          class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom"
        >
          <h1 class="h2">SMM Scraper</h1>
        </div>
        <FiltersBlock
          :selectedNetwork="selectedNetwork"
          :filters="filters"
          :selectedFilter="selectedFilter"
          @selectFilter="handleFilterSelect"
          @updateRateRange="handleRateRangeUpdate"
        />
        <MainSide
          :selectedNetwork="selectedNetwork"
          :selectedFilter="selectedFilter"
          :rateRange="rateRange"
        />
      </main>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { fetchNetworks } from "./services/api";
import LeftSide from "./components/LeftSide.vue";
import FiltersBlock from "./components/FiltersBlock.vue";
import MainSide from "./components/MainSide.vue";

export default {
  components: {
    LeftSide,
    FiltersBlock,
    MainSide,
  },
  setup() {
    const selectedNetwork = ref("All services");
    const selectedFilter = ref(null);
    const filters = ref([]);
    const networks = ref([]);
    const rateRange = ref({ from: null, to: null });

    onMounted(async () => {
      try {
        const response = await fetchNetworks();
        networks.value = response.networks;
        filters.value = response.filters;
      } catch (error) {
        console.error("Error fetching networks and filters:", error);
      }
    });

    const handleNetworkSelect = (network) => {
      selectedNetwork.value = network;
    };

    const handleFilterSelect = (filter) => {
      selectedFilter.value = filter;
    };

    const handleRateRangeUpdate = (range) => {
      rateRange.value = range;
    };

    return {
      selectedNetwork,
      selectedFilter,
      filters,
      networks,
      rateRange,
      handleNetworkSelect,
      handleFilterSelect,
      handleRateRangeUpdate,
    };
  },
};
</script>
