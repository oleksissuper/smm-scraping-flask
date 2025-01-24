<script>
export default {
  props: {
    networks: {
      type: Array,
      required: true,
    },
  },
  methods: {
    handleNetworkClick(network) {
      this.$emit("selectNetwork", network);
    },
  },
};
</script>

<template>
  <div
    class="sidebar border border-right col-md-3 col-lg-2 p-0 bg-body-tertiary"
  >
    <div
      class="offcanvas-md offcanvas-end bg-body-tertiary"
      tabindex="-1"
      id="sidebarMenu"
      aria-labelledby="sidebarMenuLabel"
    >
      <div
        class="offcanvas-body d-md-flex flex-column p-0 pt-lg-3 overflow-y-auto"
      >
        <ul class="nav flex-column">
          <li
            v-for="(network, index) in networks"
            :key="index"
            class="nav-item"
          >
            <a
              @click.prevent="handleNetworkClick(network)"
              class="nav-link d-flex align-items-center gap-2"
              href="#"
            >
              {{ network }}
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  height: 100vh;
}
</style>
