<template>
  <div class="container justify-content-center align-middle mt-3">
    <div class="h-100 align-middle">
      <b-card class="text-center">
        <div class="mt-3 d-flex flex-grow-1 justify-content-between">
          <label class="title-2">Тип</label>
          <select class="form-select ml-5" v-model="task.type_id[0]">
            <option v-for="type in types" :key="type._id"
                    v-bind:value="type._id"
            >
              {{type.type}}
            </option>
          </select>
        </div>
        <div class="mt-3 d-flex flex-grow-1 justify-content-between">
          <label class="title-2">Название</label>
          <input class="form-control ml-5" v-model="task.question_name[0]"
          @change="checkName"/>
        </div>
<!--        <div>-->
<!--          <label class="red-text" v-if="check_result">-->
<!--            Задача с таким названием уже существует-->
<!--          </label>-->
<!--        </div>-->
        <div v-if="task.type_id == 1">
          <NewCoderunnerTaskCard :task="task" />
        </div>
        <div v-if="task.type_id == 2">
          <NewMultichoiceTaskCard :task="task" />
        </div>
      </b-card>
    </div>
  </div>
</template>

<script lang="ts">
import {Vue, Component} from 'vue-property-decorator';
import {Topic} from "@/types/task";
import {types} from "@/store";
import NewMultichoiceTaskCard
  from "@/components/new-task/newMultichoiceTaskCard.vue";
import NewCoderunnerTaskCard
  from "@/components/new-task/newCoderunnerTaskCard.vue";
import {checkNameInDB} from "@/components/new-task/helpers/requests";

@Component({
  components: {
    NewCoderunnerTaskCard,
    NewMultichoiceTaskCard
  },
  props: ['task']
})
export default class CreateNew extends Vue {
  private types = types
  private check_result = false
  private topic_list: Topic[] = []

  private async checkName() {
    this.check_result = await checkNameInDB(this.$props.task.question_name[0])
  }
}
</script>

<style scoped>

</style>