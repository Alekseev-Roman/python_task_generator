<template>
  <b-modal title="Добавление по ссылке" id="add-by-url"
           @cancel="cancel" @close="cancel" @ok="addTask" centered
  >
    <div class="form-group">
      <label for="inputTaskUrl" class="title-2">
        Введите ссылку на задачу
      </label>
      <input
          type="text"
          class="form-control"
          aria-describedby="emailHelp"
          placeholder="https://e.moevm.info/question/question.php"
          v-model="taskUrl"
      />
    </div>
    <template v-slot:modal-footer="{ ok, cancel }">
      <b-button
          variant="primary"
          class="custom-button small mr-3 text"
          @click="cancel"
      >
        Отмена
      </b-button>
      <b-button @click="ok" variant="primary" class="custom-button text">
        Добавить
      </b-button>
    </template>
  </b-modal>
</template>

<script lang="ts">
import {Vue, Component} from 'vue-property-decorator';
import {importTaskByUrl} from "@/components/new-task/helpers/requests";

@Component({
  props: ['task']
})
export default class AddByUrl extends Vue {
  public taskUrl = ""

  public async cancel() {
    this.taskUrl = ""
  }

  public async addTask() {
    await importTaskByUrl(
        this.$props.task.topic_id, this.$props.task.difficulty, this.taskUrl
    )
    this.taskUrl = ""
    this.$router.go(0)
  }
}
</script>

<style scoped>

</style>