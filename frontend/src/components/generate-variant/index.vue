<template>
  <div class="container justify-content-center align-middle">
    <div class="h-100 align-middle">
      <p class="title-1 text-center bold mt-1">
        Генерирование варианта
      </p>
      <hr align="center" class="hr-1" size="4">
      <TaskCard v-bind:topic-list="topicList" v-bind:params="params[0]"
                v-bind:task="variant[1]" />
      <TaskCard v-bind:topic-list="topicList" v-bind:params="params[1]"
                v-bind:task="variant[2]" />
      <TaskCard v-bind:topic-list="topicList" v-bind:params="params[2]"
                v-bind:task="variant[3]" />
      <div class="text-center mb-3">
        <button class="act-button text-white w-25 mt-3"
                @click="getVariant"
        >
          Сгенерировать
        </button>
        <button class="act-button text-white w-25 mt-3"
                v-if="variant[1] != undefined" @click="downloadVariant"
        >
          Скачать вариант
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from "vue-property-decorator";
import TaskCard from "@/components/generate-variant/taskCard.vue";
import {fetchTopicAll} from "@/components/helpers/requests";
import {Task, Topic} from "@/types/task";
import MultichoiceTaskCard from "@/components/generate-task/multichoiceTaskCard.vue";
import CoderunnerTaskCard from "@/components/generate-task/coderunnerTaskCard.vue";
import {downloadVariantByID, fetchVariant} from "@/components/generate-variant/helpers/requests";

@Component({
  components: {
    CoderunnerTaskCard, MultichoiceTaskCard,
    TaskCard
  }
})
export default class GenerateVariant extends Vue {
  private topicList: Topic[] = []
  private variant: Task[] = []

  private params = {
    0: {
      topic: null,
      type: null,
      difficulty: 1
    },
    1: {
      topic: null,
      type: null,
      difficulty: 2
    },
    2: {
      topic: null,
      type: null,
      difficulty: 3
    }
  }

  private async created() {
    this.topicList = await fetchTopicAll()
  }

  private async getVariant() {
    this.variant = await fetchVariant(this.params)
  }

  private async downloadVariant() {
    console.log(this.variant[1], this.variant[2], this.variant[3])
    await downloadVariantByID(
        this.variant[1],
        this.variant[2],
        this.variant[3]
    )
  }
}
</script>

<style scoped>

</style>