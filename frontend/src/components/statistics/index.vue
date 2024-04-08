<template>
  <div>
    <header class="d-flex justify-content-between">
      <div class="title-1 title mr-3">Статистика по задачам</div>
    </header>
    <b-container fluid>

      <b-col lg="6" class="my-1">
        <b-form-group
            label="Filter"
            label-for="filter-input"
            label-cols-sm="1"
            label-align-sm="right"
            label-size="sm"
            class="mb-0"
        >
          <b-input-group size="sm">
            <b-form-input
                id="filter-input"
                v-model="filter"
                type="search"
                placeholder="Type to Search"
            ></b-form-input>

            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
            </b-input-group-append>
          </b-input-group>
        </b-form-group>
      </b-col>
      <b-table
          :items="items"
          :fields="fields"
          :filter="filter"
          :filter-included-fields="filterOn"
          :sort-by.sync="sortBy"
          :sort-desc.sync="sortDesc"
          :sort-direction="sortDirection"
          stacked="md"
          show-empty
          small
      >
        <template #cell(fileName)="row">
          <span class="topicName">{{ row.item.topicName }}/</span>
          <span class="numberTasks">{{ row.item.numberTasks }}/</span>
          <span class="uniqTask">{{ row.item.uniqTask }}</span>
        </template>
      </b-table>
    </b-container>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { mapActions, mapGetters, mapMutations } from "vuex";


@Component
export default class Statistics extends Vue {
  public items = []
  public fields = [
    { key: 'selection', label: ''},
    { key: 'topicName', label: 'Название темы', sortable: true},
    { key: 'numberTasks', label: 'Количество задач', sortable: true},
    { key: 'uniqTask', label: '% уникальности', sortable: true }
  ]

  public sortBy = ''
  public sortDesc = false
  public sortDirection = 'asc'
  public filter = ''
  public filterOn = []

  private get sortOptions() {
    return this.fields
        .filter(f => f.sortable)
        .map(f => {
          return { text: f.label, value: f.key }
        })
  }

  public async showCheckInfo(rowData: any) {
    this.$router.push({name: 'checkInfo', params: {id: rowData.item.fileId }})
  }
  public info(row: any) {
    console.log('row in info: ', row)
  }
  private statistics: any = []
  async created() {
    console.log('items in stats: ', this.items)
  }
}
</script>

<style lang="scss" scoped>
.thead-dark {
  background: #0f0049 !important;
}
.title {
  color: #000000;
}
.repoName {
  color: #7375A5;
}
.dirName {
  color: #9D9D9D;
}
.fileName {
  color: #5A5A5A;
}
.custom-button-icon {
  background: transparent;
  box-shadow: none;
  padding: 0;
}
.file-icon {
  width: 20px;
  height: 20px;
}
.alter-title {
  text-align: center;
}
</style>
