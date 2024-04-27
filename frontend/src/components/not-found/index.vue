<template>
  <div class="row justify-content-center">
    <div class="col-md-12 col-sm-12">
      <div class="card shadow-lg border-0 rounded-lg mt-5 mx-auto"
           style="width: 30rem;"
      >
        <h3 class="card-header display-1 text-muted text-center">
          404
        </h3>

        <span class="text mb-2 text-center">
          Страница не найдена
        </span>

        <div class="card-body mx-auto">
          <a type="button" href="/"
             class="act-button btn-sm w-text">
            На главную страницу
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {Vue, Component} from 'vue-property-decorator';

@Component({})
export default class NotFound extends Vue {

}
</script>

<style scoped>
.card {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0, 0, 0, 0.04);
  border-radius: .25rem;
}

.card .card-header {
  background-color: #fff;
  border-bottom: none;
}
</style>