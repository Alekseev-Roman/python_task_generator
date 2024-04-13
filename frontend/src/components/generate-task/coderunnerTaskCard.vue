<template>
  <div>
    <div class="d-flex flex-grow-1 justify-content-left">
      <span class="text">Тип coderunner: </span>
      <span class="text ml-3">
        {{task.coderunner_type}}
      </span>
    </div>
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
      <label class="text">Заполнение шаблона</label>
      <textarea class="form-control" rows="5"
                v-model="task.template_params" readonly
      ></textarea>
    </div>
    <div class="text-left mt-3">
      <label class="text">Код проверки</label>
      <textarea class="form-control" rows="12"
                v-model="task.template" readonly
      ></textarea>
    </div>
    <div class="text-left mt-3">
      <label class="text">Предварительное заполнение поля ответа</label>
      <textarea class="form-control" rows="6"
                v-model="task.answer_preload" readonly
      ></textarea>
    </div>
    <div class="text-left mt-3">
      <label class="text" v-if="task.test_cases">Тестовые примеры</label>
      <b-card v-for="index in Object.keys(task.test_cases.test_code)"
              :key="index" class="mt-2"
      >
        <label class="text">Пример</label>
        <textarea class="form-control" rows="5"
                  v-model="task.test_cases.test_code[index]" readonly
        ></textarea>
        <label class="text mt-2">Ввод</label>
        <textarea class="form-control" rows="5"
                  v-model="task.test_cases.stdin[index]" readonly></textarea>
        <label class="text mt-2">Результат</label>
        <textarea class="form-control" rows="5"
                  v-model="task.test_cases.expected[index]" readonly
        ></textarea>
        <span class="text mt-2"
              v-if="task.test_cases.use_as_example[index]"
        >
          Используется как пример
        </span>
      </b-card>
    </div>
  </div>
</template>

<script lang="ts">
import {Vue, Component} from 'vue-property-decorator';
import {marked} from "marked";

@Component({
  props: ['task'],
})
export default class CoderunnerTaskCard extends Vue {
  private markdownToHtml(question_text: string) {
    if (question_text != null) {
      return marked(question_text)
    }
    return ""
  }
}
</script>

<style scoped>

</style>