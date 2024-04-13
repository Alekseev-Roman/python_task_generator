<template>
  <div class="container justify-content-center align-middle">
    <div class="h-100 align-middle">
      <p class="title-1 text-center bold mt-1">
        Добавление задачи
      </p>
      <hr align="center" class="hr-1" size="4">
      <b-card class="text-center">
        <form class="container-vs text-center" @submit.prevent="submitForm">
          <div class=" d-flex flex-grow-1 justify-content-between mt-3">
            <span class="title-2">Сложность</span>
            <div v-for="difficulty in difficulties"
                 :key="difficulty._id" class="form-check ml-5"
            >
              <input
                  class="form-check-input" type="radio" name="radioDifficulty"
                  :value="difficulty.difficulty" id="radioDifficulty1"
                  v-model="task.difficulty[0]"
                  required @change="getQuantityTasks"
              />
              <label class="form-check-label title-2" for="radioDifficulty1">
                {{ difficulty.difficulty }}
              </label>
            </div>
          </div>
          <div class=" d-flex flex-grow-1 justify-content-between mt-3">
            <span class="title-2">Тема</span>
            <select class="form-select  ml-5" v-model="task.topic_id[0]"
                    @change="getQuantityTasks" required
            >
              <option v-for="topic in topic_list" :key="topic._id"
                      v-bind:value="topic._id"
              >
                {{topic.name}}
              </option>
            </select>
          </div>
          <div class="text-right mt-2" @click="$bvModal.show('add-new-topic')">
            <button type="button" class="act-button text-white">
              Новая тема
            </button>
          </div>
<!--          <div class=" d-flex flex-grow-1 justify-content-left mt-3">-->
<!--            <span class="text mr-3">-->
<!--              Средняя уникальность подходящих задач:-->
<!--            </span>-->
<!--            <span v-bind:class="[ task_match.mathPercent < 60 ?-->
<!--             'red-text' : 'text']"-->
<!--            >-->
<!--                {{task_match.mathPercent}} %-->
<!--              </span>-->
<!--          </div>-->
          <div class=" d-flex flex-grow-1 justify-content-left mt-3">
            <span class="text mr-3">Количество подходящих задач в теме: </span>
            <span v-bind:class="[ quantityTasks < 1 ? 'red-text' : 'text']">
                {{quantityTasks}}
              </span>
          </div>
          <div class="mt-3">
            <input id="importFile" type="file"
                   @change="importFile" hidden accept=".xml"
                   v-if="task.difficulty[0] && task.topic_id[0]"
            >
            <button class="custom-button text" @click="download"
                    v-b-tooltip type="submit">Загрузить файл
            </button>
            <button class="ml-2 custom-button text"
                    @click="task.difficulty[0] && task.topic_id[0] ?
                    $bvModal.show('add-by-url') : () => {}; creating = false"
                    type="submit"
            >
              Загрузить по ссылке
            </button>
            <button class="ml-2 custom-button text"
                    @click="task.difficulty[0] && task.topic_id[0] ?
                    creating = true : () => {}"
                    type="submit"
            >
              Создать задачу
            </button>
          </div>
        </form>
      </b-card>
      <div v-if="creating">
        <CreateNew :task="task" />
      </div>
    </div>
    <AddByUrl />
    <AddNewTopic />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import AddByUrl from "@/components/new-task/addByUrl.vue";
import CreateNew from "@/components/new-task/createNew.vue";
import { downloadData, fetchQuantityTask }
  from "@/components/new-task/helpers/requests";
import {Topic} from "@/types/task";
import {difficulties, types} from "@/store";
import {fetchTopicAll } from "@/components/helpers/requests";
import {tasksMatch} from "@/types/check";
import AddNewTopic from "@/components/new-task/addNewTopic.vue";


@Component({
  components: {
    AddByUrl,
    AddNewTopic,
    CreateNew
  }
})
export default class NewTask extends Vue {
  private selectedData = {
    topic: null,
    difficulty: null
  }

  private types = types
  private task_match: tasksMatch[] = []
  private topic_list: Topic[] = []
  private creating = false

  private quantityTasks = 0

  private difficulties = difficulties

  private selectedDifficulties = null
  private selectedTopic = null

  private task = {
    type_id: [],
    difficulty: [],
    topic_id: [],
    question_name: [],
    question_text: []
  }

  private async created() {
    await this.getAllTopics()
  }

  public async getAllTopics() {
    this.topic_list = await fetchTopicAll()
  }


  public async getQuantityTasks() {
    if (this.task.topic_id[0] != null && this.task.difficulty[0] != null) {
      this.quantityTasks =
          await fetchQuantityTask(
              this.task.topic_id[0], this.task.difficulty[0]
          )
    }
  }

  private importFile( event: any ) {
    downloadData( event.target.files[ 0 ] )
  }

  private download() {
    this.creating = false
    document.getElementById( 'importFile' )?.click();
  }

  private async submitForm() {
    this.selectedData.topic = this.task.topic_id[0]
    this.selectedData.difficulty = this.task.difficulty[0]
  }
}
</script>

<style scoped>
.container-vs {
  margin-left: 15%;
  margin-right: 15%;
}
</style>