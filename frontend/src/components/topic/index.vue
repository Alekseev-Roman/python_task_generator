<template>
  <div>
    <div class="container justify-content-center align-middle">
      <div class="h-100 align-middle">
        <p class="title-1 text-center bold mt-1">
          Тема: {{topic_name}}
        </p>
        <hr align="center" class="hr-1" size="4">
        <div class="text-center mb-3">
          <button class="act-button text-white w-25 mt-3"
                  @click="deleteTopic"
          >
            Удалить тему
          </button>
        </div>
      </div>
    </div>
    <b-table
        hover :items="tasks" :fields="fields"
        class="text"
    >
    </b-table>
  </div>
</template>

<script lang="ts">
import {Vue, Component} from 'vue-property-decorator';
import TaskCard from "@/components/generate-variant/taskCard.vue";
import { fetchTasksByTopic, fetchTopicName, deleteTask, deleteTopic }
  from "@/components/topic/helpers/requests";

@Component({
  components: {TaskCard}
})
export default class Topic extends Vue {
  public topic_name = ""
  public tasks = []

  public fields = [
    {
      key: 'task_id',
      label: 'ID',
      sortable: true
    },
    {
      key: 'question_name',
      label: 'Название задачи',
      sortable: true
    },
    {
      key: 'type_name',
      label: 'Тип задачи',
      sortable: true
    },
    {
      key: 'difficulty',
      label: 'Сложность',
      sortable: true
    }]

  private async created() {
    await this.fetchTopicName()
    await this.fetchTasksByTopic()
  }

  private async fetchTopicName() {
    this.topic_name = await fetchTopicName(this.$route.query.id)
  }

  private async fetchTasksByTopic() {
    this.tasks = await fetchTasksByTopic(this.$route.query.id)
  }

  public async deleteTopic() {
    await deleteTopic(this.$route.query.id)
    this.$router.push('/statistics')
  }

  public async deleteTask(task_id: any) {
    await deleteTask(task_id)
  }
}
</script>

<style scoped>

</style>