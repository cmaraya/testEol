<template>
  <Line id="linearChart" :data="chart_data" :options="chart_options" v-if="!loading" />
</template>

<script>
import { Line } from "vue-chartjs";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default {
  name: "LineChart",
  components: { Line },
  props: ["chart_data", "chart_options","loading"],
  data() {
    return {
    };
  },
};
</script>
