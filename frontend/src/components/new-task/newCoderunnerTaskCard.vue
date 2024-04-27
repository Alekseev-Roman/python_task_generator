<template>
  <form @submit.prevent="submitForm">
    <div class="mt-3 d-flex flex-grow-1 justify-content-between">
      <label class="title-2">Тип coderunner </label>
      <select class="form-select ml-5" v-model="selected_coderunner_type"
              required
      >
        <option v-for="coderunner in coderunners_list"
                :key="coderunner._id" v-bind:value="coderunner._id"
        >
          {{coderunner.name}}
        </option>
      </select>
    </div>
    <div class="text-left mt-3">
      <label class="text">Условие</label>
      <textarea class="form-control" rows="7" v-model="question_text"
                required
      ></textarea>
    </div>
    <div class="text-left mt-3">
      <label class="text">Заполнение шаблона</label>
      <textarea class="form-control" rows="5" v-model="template_params"
      ></textarea>
    </div>
    <div class="text-left mt-3">
      <label class="text">Код проверки</label>
      <textarea class="form-control" rows="12" v-model="template"
                required
      ></textarea>
    </div>
    <div class="text-left mt-3">
      <label class="text">Предварительное заполнение поля ответа</label>
      <textarea class="form-control" rows="6"
                v-model="answer_preload"
      ></textarea>
    </div>
    <div class="text-left mt-3">
      <div>
        <label class="text">Тестовые примеры</label>
      </div>
      <b-card v-for="answer in answers" :key="answer._id" class="mt-3">
        <label class="text">Пример</label>
        <textarea class="form-control" rows="5"
                  v-model="answer.test_code"
        ></textarea>
        <label class="text">Ввод</label>
        <textarea class="form-control" rows="5"
                  v-model="answer.stdin"
        ></textarea>
        <label class="text">Результат</label>
        <textarea class="form-control" rows="5"
                  v-model="answer.expected"
        ></textarea>
        <div class="mt-3 d-flex flex-grow-1 justify-content-between">
          <div class="mt-3 d-flex flex-grow-1 justify-content-left">
            <span class="title-2">Использовать как пример </span>
            <input
                class="form-check ml-3" type="checkbox"
                name="checkboxUseAsExample"
                id="checkboxUseAsExample" v-model="answer.use_as_example"
            />
          </div>
          <button class="custom-button act-button w-text w-15"
                  @click="deleteAnswer(answer)" type="button"
          >
            Удалить
          </button>
        </div>
      </b-card>
      <div>
        <button class="custom-button act-button w-text mt-3 w-25"
                @click="newAnswer" type="button"
        >
          Добавить тестовый пример
        </button>
      </div>
    </div>
    <div class="mt-3 d-flex flex-grow-1 justify-content-center">
      <button class="custom-button act-button w-text mt-3 w-25"
              type="submit"
      >
        Сохранить
      </button>
    </div>
  </form>
</template>

<script lang="ts">
import {Vue, Component} from 'vue-property-decorator';
import {Coderunner, CoderunnerAnswer} from "@/types/task";
import {importTask} from "@/components/new-task/helpers/requests";
import {fetchCoderunnerAll} from "@/components/helpers/requests";

@Component({
  props: ['task', 'check']
})
export default class NewCoderunnerTaskCard extends Vue {
  public selected_coderunner_type = null
  public question_text = ''
  public template_params = ''
  public template = ''
  public answer_preload = ''

  public coderunners_list: Coderunner[] = []

  public answers: CoderunnerAnswer[] = []

  private async created() {
    await this.getAllCoderunnerTypes()
  }

  public async getAllCoderunnerTypes() {
    this.coderunners_list = await fetchCoderunnerAll()
  }

  public newAnswer() {
    this.answers.push(
        {
          _id: this.answers.length == 0 ? 0 :
              this.answers[this.answers.length - 1]._id + 1,
          example: "",
          test_code: "",
          expected: "",
          use_as_example: false
        }
    )
  }

  public deleteAnswer( item: CoderunnerAnswer ) {
    this.answers.splice(this.answers.indexOf(item), 1)
  }

  private async importTask() {
    this.$props.task['question_text'] = [this.question_text]
    this.$props.task['template_params'] = [this.template_params]
    this.$props.task['template'] = [this.template]
    this.$props.task['coderunner_id'] = this.selected_coderunner_type
    this.$props.task['answer_preload'] = [this.answer_preload]
    this.$props.task['test_case'] = this.answers
    if (await importTask(this.$props.task) == '1') {
      this.$emit('reload')
    }
  }

  public async submitForm() {
    if (!this.$props.check) {
      await this.importTask()
    }
  }
}
</script>

<style scoped>

</style>