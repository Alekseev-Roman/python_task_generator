<template>
  <div>
    <b-table
        hover :items="items" :fields="fields"
        class="text" @row-clicked="chooseTopic"
    >
    </b-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import {fetchStatistic} from "@/components/statistics/helpers/requests";
import {Topics} from "@/types/task";


@Component
export default class Statistics extends Vue {
  public fields = [
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
  public items: Topics[] = []

  private async created() {
    this.items = await fetchStatistic()
  }

  public chooseTopic(data: any) {
    this.$router.push(`/topic?id=${data.topic_id}`)
  }
}
</script>

<style lang="scss" scoped>

</style>
