<template>
  <div>
    <div class="text-left mt-3">
      <label class="text">Условие</label>
      <textarea class="form-control" rows="7"
                v-model="task.question_text" readonly
      ></textarea>
    </div>
    <div class="text-left mt-3">
      <label class="text">Условие, отображаемое студенту</label>
      <b-card>
        <div class="text" v-html="markdownToHtml(task.question_text)"></div>
      </b-card>
    </div>
    <div class="text-left mt-3">
      <label class="text">Варианты ответа</label>
    </div>
    <b-card v-for="index in Object.keys(task.answers.answer)"
            :key="index" class="text-left mt-2"
    >
      <label class="text">Вариант ответа</label>
      <textarea class="form-control" rows="2"
                v-model="task.answers.answer[index]" readonly
      ></textarea>
      <div class="text-left mt-3">
        <label class="text">Вариант, отображаемый студенту</label>
        <b-card>
          <div class="text"
               v-html="markdownToHtml(task.answers.answer[index])"
          ></div>
        </b-card>
      </div>
      <div class="text-left mt-3">
        <label class="text">Оценка</label>
        <input class="ml-5" type="number" id="grade" name="grade"
               min="-100" max="100"
               v-model="task.answers.answer_fraction[index]" readonly
        />
        <span class="text ml-2">%</span>
      </div>
    </b-card>
  </div>
</template>

<script lang="ts">
import {Vue, Component} from 'vue-property-decorator';
import { answerNumbers } from "@/store";
import {marked} from "marked";

@Component({
  props: ['task']
})
export default class MultichoiceTaskCard extends Vue {
  public answerNumbers = answerNumbers
  public selectedAnswerNumber = 0

  public markdownToHtml(text: string) {
    if (text != null) {
      return marked(text)
    }
    return ""
  }
}
</script>


<style scoped>

</style>