<template>
  <form @submit.prevent="submitForm">
    <div class="text-left mt-3">
      <label class="text">Условие</label>
      <textarea class="form-control" rows="7"
                v-model="question_text"
      ></textarea>
    </div>

<!--    <div class=" d-flex flex-grow-1 justify-content-left mt-3">-->
<!--      <label class="text">Количество правильных ответов </label>-->
<!--      <div v-for="answerNumber in answerNumbers"-->
<!--           :key="answerNumber._id" class="form-check ml-5"-->
<!--      >-->
<!--        <input class="form-check-input" type="radio" name="radioDifficulty"-->
<!--               :value="answerNumber.number" id="radioDifficulty1"-->
<!--               v-model="selectedAnswerNumber"-->
<!--        />-->
<!--        <label class="form-check-label title-2" for="radioDifficulty1">-->
<!--          {{ answerNumber.number }}-->
<!--        </label>-->
<!--      </div>-->
<!--    </div>-->
    <div class=" d-flex flex-grow-1 justify-content-left mt-3">
      <label class="text">Штраф за неправильный ответ </label>
      <input class="ml-5" type="number" step="0.01" id="grade"
             name="grade" min="0" max="1" v-model="penalty"/>
    </div>
    <div class="text-left mt-3">
      <div>
        <label class="text">Варианты ответа</label>
      </div>
      <b-card v-for="answer in answers" :key="answer._id" class="mt-3">
        <label class="text">Вариант ответа</label>
        <textarea class="form-control" rows="2"
                  v-model="answer.answer"
        ></textarea>
        <div class="mt-3 d-flex flex-grow-1 justify-content-between">
          <div class="text-left">
            <label class="text">Оценка</label>
            <input class="ml-5" type="number" id="grade"
                   name="grade" min="-100" max="100"
                   v-model="answer.answer_fraction"
            />
            <span class="text ml-2 mr-5">%</span>
            <button class="act-button ml-3 w-text"
                    @click="answer.answer_fraction = 100"
            >
              100 %
            </button>
            <button class="act-button ml-3 w-text"
                    @click="answer.answer_fraction = -100"
            >
              -100 %
            </button>
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
          Добавить вариант ответа
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
import { answerNumbers } from "@/store";
import {MultichoiceAnswer} from "@/types/task";
import {importTask} from "@/components/new-task/helpers/requests";

@Component({
  props: ['task']
})
export default class NewMultichoiceTaskCard extends Vue {
  private answerNumbers = answerNumbers
  private selectedAnswerNumber = 0
  private question_text = ''
  private penalty = 0.0

  private answers: MultichoiceAnswer[] = []

  private newAnswer() {
    this.answers.push(
        {
          _id: this.answers.length == 0 ? 0 :
              this.answers[this.answers.length - 1]._id + 1,
          answer: "",
          answer_fraction: 0,
        }
    )
  }

  private deleteAnswer( item: MultichoiceAnswer ) {
    this.answers.splice(this.answers.indexOf(item), 1)
  }

  private async importTask() {
    this.$props.task['question_text'] = [this.question_text]
    this.$props.task['penalty'] = this.penalty
    this.$props.task['answers'] = this.answers
  }

  private async submitForm() {
    await this.importTask()
  }
}
</script>


<style scoped>

</style>