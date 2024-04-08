<template>
  <div>
    <div class="mt-3 d-flex flex-grow-1 justify-content-between">
      <label class="title-2">Тип coderunner </label>
      <select class="form-select ml-5" v-model="selectedCoderunnerType">
        <option v-for="coderunnerType in coderunnerTypes" :key="coderunnerType._id" v-bind:value="coderunnerType._id">
          {{coderunnerType.name}}
        </option>
      </select>
    </div>
    <div class="text-left mt-3">
      <label class="text">Условие</label>
      <textarea class="form-control" rows="7"></textarea>
    </div>
    <div class="text-left mt-3">
      <label class="text">Заполнение шаблона</label>
      <textarea class="form-control" rows="5"></textarea>
    </div>
    <div class="text-left mt-3">
      <label class="text">Код проверки</label>
      <textarea class="form-control" rows="12"></textarea>
    </div>
    <div class="text-left mt-3">
      <div>
        <label class="text">Тестовые примеры</label>
      </div>
      <b-card v-for="answer in answers" :key="answer._id" class="mt-3">
        <label class="text">Пример</label>
        <textarea class="form-control" rows="5" v-model="answer.example"></textarea>
        <label class="text">Ввод</label>
        <textarea class="form-control" rows="5" v-model="answer.input"></textarea>
        <label class="text">Результат</label>
        <textarea class="form-control" rows="5" v-model="answer.result"></textarea>
        <div class="mt-3 d-flex flex-grow-1 justify-content-between">
          <div class="mt-3 d-flex flex-grow-1 justify-content-left">
            <span class="title-2">Использовать как пример </span>
            <input
                class="form-check ml-3" type="checkbox" name="checkboxUseAsExample"
                id="checkboxUseAsExample" v-model="answer.use_as_example"
            />
          </div>
          <button class="custom-button act-button w-text w-15" @click="deleteAnswer(answer)">
            Удалить
          </button>
        </div>
      </b-card>
      <div>
        <button class="custom-button act-button w-text mt-3 w-25" @click="newAnswer">
          Добавить тестовый пример
        </button>
      </div>
    </div>
    <div class="mt-3 d-flex flex-grow-1 justify-content-left">
      <button class="custom-button act-button w-text mt-3 w-25">
        Сохранить
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import {Vue, Component} from 'vue-property-decorator';
import {CoderunnerAnswer, CoderunnerTypes} from "@/types/task";

@Component({
})
export default class NewCoderunnerTaskCard extends Vue {
  private selectedCoderunnerType = null

  private coderunnerTypes: CoderunnerTypes[] = []

  private answers: CoderunnerAnswer[] = []

  private newAnswer() {
    this.answers.push(
        {
          _id: this.answers.length == 0 ? 0 : this.answers[this.answers.length - 1]._id + 1,
          example: "",
          input: "",
          result: "",
          use_as_example: false
        }
    )
  }

  private deleteAnswer( item: CoderunnerAnswer ) {
    this.answers.splice(this.answers.indexOf(item), 1)
  }
}
</script>

<style scoped>

</style>