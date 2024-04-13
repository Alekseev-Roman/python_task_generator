<template>
  <div class="navbar">
    <div class="d-flex flex-grow-1 justify-content-between">
      <div @click="showMainPage" class="li">
        <span class="title-1">LabWorks Generator</span>
      </div>
      <b-button-group>
        <button class="custom-button hover title-2 btn-link"
                @click="generateTask"
        >
          Сгенерировать задачу
        </button>
        <button class="custom-button title-2 btn-link" @click="generateVariant">
          Сгенерировать вариант
        </button>
        <button class="custom-button title-2 btn-link" @click="addTask">
          Добавить задачу
        </button>
        <button class="custom-button title-2 btn-link" @click="showStatistic">
          Статистика
        </button>
      </b-button-group>
    </div>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'

@Component
export default class Navbar extends Vue {
  private showMainPage() {
    if(!(this.$router.currentRoute.name == 'mainPage')) {
      this.$router.push({name: 'mainPage'})
    }
  }

  private generateTask() {
    if(!(this.$router.currentRoute.name == 'generateTask')) {
      this.$router.push({name: 'generateTask'})
    }
  }

  private generateVariant() {
    if(!(this.$router.currentRoute.name == 'generateVariant')) {
      this.$router.push({name: 'generateVariant'})
    }
  }

  private addTask() {
    if(!(this.$router.currentRoute.name == 'newTask')) {
      this.$router.push({name: 'newTask'})
    }
  }

  private showStatistic() {
    if(!(this.$router.currentRoute.name == 'statistic')) {
      this.$router.push({name: 'statistics'})
    }
  }
}
</script>

<style lang="scss" scoped>
.navbar {
  height: 65px;
  background: #f8f8f8;
}
</style>