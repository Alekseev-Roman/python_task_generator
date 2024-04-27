<template>
  <b-modal title="Добавление по ссылке" id="add-by-url"
           @cancel="cancel" @close="cancel" centered
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

@Component({})
export default class AddByUrl extends Vue {
  public taskUrl = ""

  public async cancel() {
    //
  }
}
</script>

<style scoped>

</style>