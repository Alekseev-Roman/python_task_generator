<template>
  <div class="container justify-content-center align-middle mt-3">
    <div class="h-100 align-middle">
      <b-card class="text-center">
        <div class="mt-3 d-flex flex-grow-1 justify-content-between">
          <span class="title-2">Тип</span>
          <select class="form-select ml-5" v-model="selectedType">
            <option v-for="type in types" :key="type._id" v-bind:value="type._id">{{type.type}}</option>
          </select>
        </div>
        <div v-if="selectedType == 1">
          <NewCoderunnerTaskCard />
        </div>
        <div v-if="selectedType == 2">
          <NewMultichoiceTaskCard />
        </div>
      </b-card>
    </div>
  </div>
</template>

<script lang="ts">
import {Vue, Component} from 'vue-property-decorator';
import {Task, Topic} from "@/types/task";
import {types} from "@/store";
import NewMultichoiceTaskCard from "@/components/new-task/newMultichoiceTaskCard.vue";
import NewCoderunnerTaskCard from "@/components/new-task/newCoderunnerTaskCard.vue";

@Component({
  components: {
    NewCoderunnerTaskCard,
    NewMultichoiceTaskCard
  }
})
export default class CreateNew extends Vue {
  private selectedType = 0

  private types = types
  private topicList: Topic[] = []
  private task: Task[] = []
}
</script>

<style scoped>

</style>