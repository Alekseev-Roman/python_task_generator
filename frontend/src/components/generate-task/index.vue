<template>
  <div class="container justify-content-center align-middle">
    <div class="h-100 align-middle">
      <p class="title-1 text-center bold mt-1">
        Генерирование задачи
      </p>
      <hr align="center" class="hr-1" size="4">
      <b-card class="text-center">
        <form class="container-vs text-center" @submit.prevent="submitForm">
          <div class="mt-3 d-flex flex-grow-1 justify-content-between">
            <span class="title-2">Тип</span>
            <select class="form-select  ml-5" v-model="selectedType" @change="getQuantityTasks" required>
              <option v-for="type in types" :key="type._id" v-bind:value="type._id">{{type.type}}</option>
            </select>
          </div>
          <div class=" d-flex flex-grow-1 justify-content-between mt-3">
            <span class="title-2">Сложность</span>
            <div v-for="difficulty in difficulties" :key="difficulty._id" class="form-check ml-5">
              <input
                  class="form-check-input" type="radio" name="radioDifficulty"
                  :value="difficulty.difficulty" id="radioDifficulty1" v-model="selectedDifficulties"
                   required @change="getQuantityTasks"
              />
              <label class="form-check-label title-2" for="radioDifficulty1">
                {{ difficulty.difficulty }}
              </label>
            </div>
          </div>
          <div class=" d-flex flex-grow-1 justify-content-between mt-3">
            <span class="title-2">Тема</span>
            <select class="form-select  ml-5" v-model="selectedTopic" @change="getQuantityTasks" required>
              <option v-for="topic in topicList" :key="topic._id" v-bind:value="topic._id">{{topic.name}}</option>
            </select>
          </div>
          <div class=" d-flex flex-grow-1 justify-content-left mt-3">
            <span class="text mr-3">Средняя уникальность подходящих задач: </span>
            <span v-bind:class="[ task_match.mathPercent < 60 ? 'red-text' : 'text']">
              {{task_match.mathPercent}} %
            </span>
          </div>
          <div class=" d-flex flex-grow-1 justify-content-left mt-3">
            <span class="text mr-3">Количество подходящих задач в теме: </span>
            <span v-bind:class="[ quantityTasks < 1 ? 'red-text' : 'text']">
              {{quantityTasks}}
            </span>
          </div>
          <button class="act-button w-text w-25 mt-3" type="submit">
            Сгенерировать
          </button>
        </form>
        <div class="-vs text-center" v-if="'question_name' in task">
          <hr align="center" class="hr-1" size="4">
          <div class="mt-3 justify-content-center">
            <span class="title-2 bold" >Сгенерированная задача: </span>
            <span class="text ml-3">{{task.question_name}}</span>
            <button class="act-button w-text mt-3 ml-3 download-button" @click="downloadTask">Скачать</button>
          </div>
          <div v-if="selectedData.type == 1">
            <CoderunnerTaskCard v-bind:task="task" />
          </div>
          <div v-if="selectedData.type == 2">
            <MultichoiceTaskCard v-bind:task="task" />
          </div>
        </div>
      </b-card>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import {
  fetchTask,
  fetchQuantityTask,
  downloadTaskByID
} from "@/components/generate-task/helpers/requests";
import {fetchTopicAll} from "@/components/helpers/requests";
import {Topic, Task} from "@/types/task";
import {tasksMatch} from "@/types/check";
import MultichoiceTaskCard from "@/components/generate-task/multichoiceTaskCard.vue";
import CoderunnerTaskCard from "@/components/generate-task/coderunnerTaskCard.vue";
import {difficulties, types} from "@/store";

@Component({
  components: {
    MultichoiceTaskCard,
    CoderunnerTaskCard
  }
})
export default class GenerateTask extends Vue {
  private difficulties = difficulties
  private types = types

  private selectedType = null
  private selectedDifficulties = null
  private selectedTopic = null

  private selectedData = {
    type: null,
    topic: null,
    difficulty: null
  }

  private quantityTasks = null

  private task_match: tasksMatch[] = []
  private topicList: Topic[] = []
  private task: Task[] = []


  private async created() {
    await this.getAllTopics()
  }

  public async getAllTopics() {
    this.topicList = await fetchTopicAll()
  }

  private async downloadTask() {
    await downloadTaskByID(this.task)
  }

  private async submitForm() {
    this.selectedData.topic = this.selectedTopic
    this.selectedData.type = this.selectedType
    this.selectedData.difficulty = this.selectedDifficulties
    this.task = await fetchTask(this.selectedType, this.selectedTopic, this.selectedDifficulties)
  }

  private async getQuantityTasks() {
    if (this.selectedTopic != null && this.selectedType != null
        && this.selectedDifficulties != null) {
      this.quantityTasks = await fetchQuantityTask(
          this.selectedType, this.selectedTopic, this.selectedDifficulties)
    }
  }
}

</script>

<style scoped>
.container-vs {
  margin-left: 15%;
  margin-right: 15%;
}
</style>