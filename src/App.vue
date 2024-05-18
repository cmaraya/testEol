<template>
  <div class="common-layout">
    <el-container>
      <el-header class="basic-style"
        ><h1>Logs de eventos del día 3 de Abril de 2023</h1></el-header
      >
      <el-main>
        <h3>Instrucciones para filtros</h3>
        <el-row class="add-padding"> </el-row>
        <el-row class="mb-4">
          <el-text alignment="flex-start" class="mx-1" tag="p">
            Para filtrar datos de eventos puedes: Ingresar la cantidad de logs a
            mostrar, especificando el número de registros de eventos deseados,
            por ejemplo, 100. Seleccionar un rango de tiempo especificando tanto
            la hora de inicio como la hora de finalización de los eventos.
            Seleccionar el origen del evento desde una lista desplegable para
            filtrar por la fuente específica. Se pueden seleccionar uno o varios
            usuarios de una lista desplegable para filtrar eventos relacionados
            con esos usuarios específicos. Seleccionar el tipo de evento desde
            una lista desplegable para filtrar por el tipo específico. <br />
            <b>Cabe destacar que todos los filtros son opcionales</b><br />
            Una vez aplicados, los filtros traerán los datos de eventos
            correspondientes únicamente al día 03 de abril del 2023.</el-text
          >
        </el-row>

        <div>
          <el-form
            :model="ruleform"
            ref="ruleForm"
            id="event_log_form"
            label-position="top"
          >
            <el-row>
              <el-col :span="8" class="add-padding">
                <el-form-item
                  label="Ingresa la cantidad de logs a mostrar"
                  prop="item_to_show"
                  id="item_to_show"
                  justify="center"
                >
                  <el-input-number
                    placeholder="Cantidad"
                    v-model="ruleform.item_to_show"
                    :min="1"
                  /> </el-form-item
              ></el-col>
              <el-col :span="8" class="add-padding">
                <el-form-item
                  label="Seleciona un rango de tiempo"
                  prop="time"
                  id="time"
                >
                  <el-time-picker
                    v-model="ruleform.time"
                    value-format="YYYY-MM-DD HH:mm:ss"
                    is-range
                    clearable
                    aria-label="Seleciona un rango de tiempo"
                    range-separator="a"
                    start-placeholder="Hora Inicial"
                    end-placeholder="Hora Final"
                  /> </el-form-item
              ></el-col>
              <el-col :span="8" class="add-padding">
                <el-form-item
                  label="Seleccione el origen del evento"
                  prop="source"
                  id="source"
                >
                  <el-select
                    v-model="ruleform.source"
                    clearable
                    filterable
                    placeholder="Origen del evento"
                  >
                    <el-option
                      v-for="item in eventSourceOptions"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value"
                    />
                  </el-select> </el-form-item
              ></el-col>
            </el-row>
            <el-row>
              <el-col :span="12" class="add-padding">
                <el-form-item
                  label="Selecciona usuario(s)"
                  prop="username"
                  id="username"
                >
                  <el-select
                    v-model="ruleform.username"
                    multiple
                    collapse-tags
                    collapse-tags-tooltip
                    filterable
                    :max-collapse-tags="3"
                    placeholder="Usuario(s)"
                  >
                    <el-option
                      v-for="item in usernameOptions"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value"
                    />
                  </el-select>
                </el-form-item>
              </el-col>
              <el-col :span="12" class="add-padding">
                <el-form-item
                  label="Seleccione el tipo del evento"
                  prop="type"
                  id="type"
                >
                  <el-select
                    v-model="ruleform.type"
                    clearable
                    filterable
                    placeholder="Tipo del evento"
                  >
                    <el-option
                      v-for="item in eventTypeOptions"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value"
                    />
                  </el-select>
                </el-form-item>
              </el-col>
            </el-row>
            <el-row>
              <el-col class="add-padding">
                <el-button size="large" type="primary" @click="applyFilters"
                  >Aplicar Filtros</el-button
                >
                <el-button size="large" @click="resetFilters"
                  >Limpiar Filtros</el-button
                >
              </el-col>
            </el-row>
          </el-form>
        </div>
        <el-divider />
        <h3>Tabla de eventos</h3>
        <el-table
          :data="tableData"
          style="width: 100%"
          v-loading="loading"
          element-loading-text="Cargando datos..."
          max-height="500"
          class="custom-loading-svg add-padding"
          element-loading-svg-view-box="-10, -10, 50, 50"
          empty-text="No se encontraron datos con los filtros ingresados"
          scrollbar-always-on
        >
          <el-table-column
            prop="id"
            label="ID"
            width="80"
            show-overflow-tooltip
          />
          <el-table-column
            fixed
            prop="time"
            label="Tiempo"
            width="170"
            show-overflow-tooltip
            :formatter="formatDate"
          />
          <el-table-column
            prop="username"
            label="Usuarios"
            width="120"
            show-overflow-tooltip
          />
          <el-table-column
            prop="event_source"
            label="Origen"
            width="100"
            show-overflow-tooltip
          />
          <el-table-column
            prop="event_type"
            label="Tipo"
            width="120"
            show-overflow-tooltip
          />
          <el-table-column
            prop="agent"
            label="Agente"
            width="150"
            show-overflow-tooltip
          />
          <el-table-column
            prop="page"
            label="Pagína"
            width="120"
            show-overflow-tooltip
          />
          <el-table-column
            prop="referer"
            label="Referencia"
            width="120"
            show-overflow-tooltip
          />
          <el-table-column
            prop="session"
            label="Sesión"
            width="120"
            show-overflow-tooltip
          />
          <el-table-column
            prop="accept_language"
            label="Idioma"
            show-overflow-tooltip
          />
        </el-table>
        <el-divider />
        <h3>Gráfico de eventos</h3>
        <div class="chart-min-height" v-loading="loading" element-loading-text="Cargando gráfico...">
          <LineChart
            :chart_data="chart_data"
            :chart_options="chart_options"
            :loading="loading"
          />
        </div>
      </el-main>
      <el-footer class="basic-style"
        ><h4>Por Catalina Araya Ilabaca</h4></el-footer
      >
    </el-container>
  </div>
</template>

<script>
import axios from "axios";
import LineChart from "./components/Chart.vue";
export default {
  name: "App",
  components: { LineChart },
  data() {
    return {
      loading: true,
      ruleform: {
        time: [],
        username: [],
        source: "",
        type: "",
        item_to_show: 1000,
      },
      usernameOptions: [],
      eventTypeOptions: [],
      eventSourceOptions: [],
      tableData: [],
      chart_data: {},
      chart_options: {
        responsive: true,
      },
    };
  },
  methods: {
    setChartData(labels,total) {
      const datasets= [
        {
          label: "Eventos",
          backgroundColor: "#009bdd",
          data: total,
        },
      ];
      let aux_data_chart = {labels:labels,datasets:datasets}      
      this.chart_data=aux_data_chart

    },
    formatDate(row) {
      const value = row.time;
      const date = new Date(value);
      const day = String(date.getDate()).padStart(2, "0");
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const year = date.getFullYear();
      const hours = String(date.getHours()).padStart(2, "0");
      const minutes = String(date.getMinutes()).padStart(2, "0");
      const seconds = String(date.getSeconds()).padStart(2, "0");
      return `${day}-${month}-${year} ${hours}:${minutes}:${seconds}`;
    },
    makeOpcionFormat(list) {
      return list.map((element) => ({
        label: element,
        value: element,
      }));
    },
    obtainUniqueElements(list, name) {
      return [...new Set(list.map((obj) => obj[name]))];
    },
    getUsernames() {
      const params = {
        item_to_show: this.ruleform.item_to_show,
      };
      axios
        .get("http://127.0.0.1:8000/api/get_unique_usernames", { params })
        .then((res) => {
          let usernames = res.data;
          let uniqueElements = this.obtainUniqueElements(usernames, "username");
          this.usernameOptions = this.makeOpcionFormat(uniqueElements);
        })
        .catch(() => {
          console.log("ERROR");
        });
    },
    getEventType() {
      const params = {
        item_to_show: this.ruleform.item_to_show,
      };
      axios
        .get("http://127.0.0.1:8000/api/get_unique_event_types", { params })
        .then((res) => {
          let event_types = res.data;
          let uniqueElements = this.obtainUniqueElements(
            event_types,
            "event_type"
          );
          this.eventTypeOptions = this.makeOpcionFormat(uniqueElements);
        })
        .catch(() => {
          console.log("ERROR");
        });
    },
    getEventSource() {
      const params = {
        item_to_show: this.ruleform.item_to_show,
      };
      axios
        .get("http://127.0.0.1:8000/api/get_unique_event_sources", { params })
        .then((res) => {
          let event_sources = res.data;
          let uniqueElements = this.obtainUniqueElements(
            event_sources,
            "event_source"
          );
          this.eventSourceOptions = this.makeOpcionFormat(uniqueElements);
        })
        .catch(() => {
          console.log("ERROR");
        });
    },
    getInitialData() {
      const params = {
        item_to_show: this.ruleform.item_to_show,
      };
      axios
        .get("http://127.0.0.1:8000/api/get_all_event_logs", { params })
        .then((res) => {
          this.tableData = res.data.event_logs;
          this.setChartData(res.data.chart_labels,res.data.chart_total)
          this.loading = false;
        })
        .catch(() => {
          console.log("ERROR");
        });
    },
    applyFilters() {
      this.loading = true;
      // Lógica para aplicar filtros y actualizar la tabla
      const params = {
        item_to_show: this.ruleform.item_to_show,
        time: this.ruleform.time,
        username: this.ruleform.username,
        source: this.ruleform.source,
        type: this.ruleform.type,
      };
      axios
        .get("http://127.0.0.1:8000/api/get_filter_event_logs", { params })
        .then((res) => {
          this.tableData = res.data.event_logs;
          let uniqueElements = this.obtainUniqueElements(
            res.data.usernames,
            "username"
          );
          this.usernameOptions = this.makeOpcionFormat(uniqueElements);
          uniqueElements = this.obtainUniqueElements(
            res.data.event_types,
            "event_type"
          );
          this.eventTypeOptions = this.makeOpcionFormat(uniqueElements);
          uniqueElements = this.obtainUniqueElements(
            res.data.event_sources,
            "event_source"
          );
          this.eventSourceOptions = this.makeOpcionFormat(uniqueElements);
          this.setChartData(res.data.chart_labels,res.data.chart_total)
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
          console.log("ERROR");
        });
    },
    resetFilters() {
      // Lógica para limpiar los filtros
      this.$refs.ruleForm.resetFields();
      this.applyFilters();
    },
  },
  mounted() {
    this.getUsernames();
    this.getEventSource();
    this.getEventType();
    this.getInitialData();
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.el-main {
  --el-main-padding: 40px;
}
.basic-style {
  background: linear-gradient(
    90deg,
    rgba(0, 179, 255, 1) 0%,
    rgba(0, 241, 255, 1) 100%
  );
  align-content: center;
  text-align: center;
  color: white;
}
.add-padding {
  padding: 0px 20px;
}
.el-select {
  width: 100%;
}
.el-input-number {
  width: 100%;
}
.el-scrollbar__view {
  display: list-item !important;
}
.el-select-dropdown__item {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
.mb-4 {
  margin-bottom: 30px;
}
.chart-min-height{
  min-height: 600px;
}
</style>
