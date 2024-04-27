<template>
  <b-modal title="Добавление по ссылке" id="add-new-topic"
           @close="close" @cancel="close" @ok="addTopic" centered
  >
    <div class="form-group">
      <label for="inputTaskUrl" class="title-2">
        Введите название темы
      </label>
      <input
          type="text"
          class="form-control"
          v-model="topicName"
          @change="checkTopicName"
      />
      <label class="red-text mt-2" v-if="checkingResult == '1'">
        Тема с таким названием уже существует
      </label>
    </div>
    <template v-slot:modal-footer="{ ok, cancel }">
      <b-button
          variant="primary"
          class="custom-button small mr-3 text"
          @click="cancel"
      >
        Отмена
      </b-button>
      <b-button @click="canAdd ? ok() : () => {}" variant="primary"
                class="custom-button text"
      >
        Добавить
      </b-button>
    </template>
  </b-modal>
</template>

<script lang="ts">
import {Vue, Component} from 'vue-property-decorator';
import { addTopic, checkTopicInDB }
  from "@/components/new-task/helpers/requests";

@Component({})
export default class AddNewTopic extends Vue {
  public topicName = ""
  public checkingResult = "0"
  public canAdd = false

  public async checkTopicName() {
    if (this.topicName != "") {
      this.checkingResult = await checkTopicInDB(this.topicName)
      if (this.checkingResult == "0") {
        this.canAdd = true
      }
    }
  }

  public async addTopic() {
    await this.checkTopicName()
    if (this.checkingResult == "0" && this.topicName != "") {
      await addTopic(this.topicName)
      this.checkingResult = "0"
      this.topicName = ""
      this.canAdd = false
    }
  }

  public close() {
    this.checkingResult = "0"
    this.topicName = ""
    this.canAdd = false
  }
}
</script>

<style scoped>

</style>