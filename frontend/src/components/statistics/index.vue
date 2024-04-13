<template>
  <div>
    <b-table  hover :items="items" :fields="fields" class="text"></b-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import {fetchStatistic} from "@/components/statistics/helpers/requests";


@Component
export default class Statistics extends Vue {
  private fields = [
    {
      key: 'topic_name',
      label: 'Тема',
      sortable: true
    },
    {
      key: 'type_name',
      label: 'Тип задачи',
      sortable: true
    },
    {
      key: 'quantity',
      label: 'Количество задач',
      sortable: true
    }]
  private items = []

  private async created() {
    this.items = await fetchStatistic()
  }

}
</script>

<style lang="scss" scoped>

</style>
