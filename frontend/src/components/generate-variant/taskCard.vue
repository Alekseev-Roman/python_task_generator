<template>
  <div class="mt-3">
    <b-card class="text-center">
      <form class="container-vs text-center" @submit.prevent="submitForm">
        <div class="mt-3 d-flex flex-grow-1 justify-content-between">
          <span class="title-2">Тип</span>
          <select class="form-select  ml-5" v-model="params.type"
                  @change="getQuantityTasks" required
          >
            <option v-for="type in types" :key="type._id"
                    v-bind:value="type._id"
            >
              {{type.type}}
            </option>
          </select>
        </div>
        <div class=" d-flex flex-grow-1 justify-content-between mt-3">
          <span class="title-2">Сложность</span>
          <div v-for="difficulty in difficulties" :key="difficulty._id"
               class="form-check ml-5"
          >
            <input
                class="form-check-input" type="radio" name="radioDifficulty"
                :value="difficulty.difficulty" id="radioDifficulty1"
                v-model="params.difficulty"
                required @change="getQuantityTasks"
            />
            <label class="form-check-label title-2" for="radioDifficulty1">
              {{ difficulty.difficulty }}
            </label>
          </div>
        </div>
        <div class=" d-flex flex-grow-1 justify-content-between mt-3">
          <span class="title-2">Тема</span>
          <select class="form-select  ml-5" v-model="params.topic"
                  @change="getQuantityTasks" required
          >
            <option v-for="topic in topicList" :key="topic._id"
                    v-bind:value="topic._id"
            >
              {{topic.name}}
            </option>
          </select>
        </div>
<!--        <div class=" d-flex flex-grow-1 justify-content-left mt-3">-->
<!--          <span class="text mr-3">Средняя уникальность подходящих задач: </span>-->
<!--          <span v-bind:class="[ task_match.mathPercent < 60 ? 'red-text' : 'text']">-->
<!--              {{task_match.mathPercent}} %-->
<!--            </span>-->
<!--        </div>-->
        <div class=" d-flex flex-grow-1 justify-content-left mt-3">
          <span class="text mr-3">Количество подходящих задач в теме: </span>
          <span v-bind:class="[ quantityTasks < 1 ? 'red-text' : 'text']">
              {{quantityTasks}}
            </span>
        </div>
      </form>
      <div v-if="task != undefined">
        <div class="-vs text-center" v-if="task.question_name">
          <hr align="center" class="hr-1" size="4">
          <div class="mt-3 justify-content-center">
            <span class="title-2 bold" >Сгенерированная задача: </span>
              <span class="text ml-3">{{task.question_name}}</span>
            <button class="act-button w-text mt-3 ml-3 download-button"
                    @click="downloadTask"
            >
              Скачать
            </button>
          </div>
            <div v-if="params.type == 1">
              <CoderunnerTaskCard v-bind:task="task" />
            </div>
            <div v-if="params.type == 2">
              <MultichoiceTaskCard v-bind:task="task" />
            </div>
        </div>
      </div>
    </b-card>
  </div>
</template>

<script lang="ts">
import {Vue, Component} from 'vue-property-decorator';
import CoderunnerTaskCard
  from "@/components/generate-task/coderunnerTaskCard.vue";
import MultichoiceTaskCard
  from "@/components/generate-task/multichoiceTaskCard.vue";
import {tasksMatch} from "@/types/check";
import {difficulties, types} from "@/store";
import {marked} from "marked";
import {downloadTaskByID, fetchQuantityTask}
  from "@/components/generate-variant/helpers/requests";

@Component({
  components: {MultichoiceTaskCard, CoderunnerTaskCard},
  props: ['task', 'topicList', 'params']
})
export default class TaskCard extends Vue {
  private difficulties = difficulties
  private types = types

  private quantityTasks = null

  private selectedData = {
    type: null,
    topic: null,
    difficulty: null
  }

  private task_created = false
  private task_match: tasksMatch[] = []

  private markdownToHtml(question_text: string) {
    return marked(question_text)
  }

  private async submitForm() {
    this.task_created = true
    this.selectedData.topic = this.$props.params.topic
    this.selectedData.type = this.$props.params.type
    this.selectedData.difficulty = this.$props.params.difficulty
  }

  private async getQuantityTasks() {
    if (this.$props.params.topic != null && this.$props.params.type != null
        && this.$props.params.difficulty != null) {
      this.quantityTasks = await fetchQuantityTask(
          this.$props.params.type, this.$props.params.topic,
          this.$props.params.difficulty)
    }
  }

  private async downloadTask() {
    await downloadTaskByID(this.$props.task)
  }
}
</script>

<style scoped>

</style>