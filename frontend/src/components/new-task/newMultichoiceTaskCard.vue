<template>
  <div>
    <div class="text-left mt-3">
      <label class="text">Условие</label>
      <textarea class="form-control" rows="7"></textarea>
    </div>

    <div class=" d-flex flex-grow-1 justify-content-left mt-3">
      <label class="text">Количество правильных ответов </label>
      <div v-for="answerNumber in answerNumbers" :key="answerNumber._id" class="form-check ml-5">
        <input class="form-check-input" type="radio" name="radioDifficulty"
               :value="answerNumber.number" id="radioDifficulty1" v-model="selectedAnswerNumber"
        />
        <label class="form-check-label title-2" for="radioDifficulty1">
          {{ answerNumber.number }}
        </label>
      </div>
    </div>
    <div class="text-left mt-3">
      <div>
        <label class="text">Варианты ответа</label>
      </div>
      <b-card v-for="answer in answers" :key="answer._id" class="mt-3">
        <label class="text">Вариант ответа</label>
        <textarea class="form-control" rows="2"></textarea>
        <div class="mt-3 d-flex flex-grow-1 justify-content-between">
          <div class="text-left">
            <label class="text">Оценка</label>
            <input class="ml-5" type="number" id="grade" name="grade" min="-100" max="100" />
            <span class="text ml-2">%</span>
          </div>
          <button class="custom-button act-button w-text w-15" @click="deleteAnswer(answer)">
            Удалить
          </button>
        </div>
      </b-card>
      <div>
        <button class="custom-button act-button w-text mt-3 w-25" @click="newAnswer">
          Добавить вариант ответа
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
import { answerNumbers } from "@/store";
import {MultichoiceAnswer} from "@/types/task";

@Component({
})
export default class NewMultichoiceTaskCard extends Vue {
  private answerNumbers = answerNumbers
  private selectedAnswerNumber = 0

  private answers: MultichoiceAnswer[] = []

  private newAnswer() {
    this.answers.push(
        {
          _id: this.answers.length == 0 ? 0 : this.answers[this.answers.length - 1]._id + 1,
          answer: "",
          answer_fraction: 0,
        }
    )
  }

  private deleteAnswer( item: MultichoiceAnswer ) {
    this.answers.splice(this.answers.indexOf(item), 1)
  }
}
</script>


<style scoped>

</style>