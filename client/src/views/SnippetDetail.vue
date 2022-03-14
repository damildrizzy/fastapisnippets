<template>
  <div class="px-6 py-8 flex flex-col justify-center items-center">
    <div class="lg:w-9/12">
      <div class="flex items-center justify-between">
        <h1 class="text-xl font-bold text-gray-700 md:text-2xl">
          {{ snippet.title }}
        </h1>
      </div>
      <div class="meta">
        <p>Author: {{ snippet.author.username }}</p>
        <p>Date Published: {{ publishedDate }}</p>
      </div>
      <div class="border-solid mt-5">
        <div class="description bg-gray-100">
          {{ snippet.description }}
        </div>
        <prism-editor
          v-model="snippet.code"
          class="my-editor overflow-auto h-96"
          :highlight="highlighter"
          line-numbers
          readonly
        >
        </prism-editor>
      </div>
    </div>
  </div>
</template>

<script>
import SnippetService from "../services/snippet.service";
import { PrismEditor } from "vue-prism-editor";
import "vue-prism-editor/dist/prismeditor.min.css";

// import highlighting library (you can use any library you want just return html string)
import { highlight, languages } from "prismjs/components/prism-core";
import "prismjs/components/prism-clike";
import "prismjs/components/prism-javascript";
import "prismjs/themes/prism-tomorrow.css"; // import syntax highlighting styles

export default {
  name: "SnippetDetail",
  components: {
    PrismEditor,
  },
  data() {
    return {
      snippet: {},
      message: "",
    };
  },
  computed: {
    publishedDate() {
      const date = new Date(this.snippet.pub_date);
      return date.toDateString();
    },
  },
  methods: {
    highlighter(code) {
      return highlight(code, languages.js); // languages.<insert language> to return html with markup
    },
    getSnippet(id) {
      SnippetService.getSnippet(id)
        .then((response) => {
          this.snippet = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  created() {
    this.message = "";
    this.getSnippet(this.$route.params.id);
  },
};
</script>

<style>
.meta p {
  display: inline-block;
  margin-right: 10px;
}

/* required class */
.my-editor {
  /* we dont use `language-` classes anymore so thats why we need to add background and text color manually */
  background: #2d2d2d;
  color: #ccc;

  /* you must provide font-family font-size line-height. Example: */
  font-family: Fira code, Fira Mono, Consolas, Menlo, Courier, monospace;
  font-size: 14px;
  line-height: 1.5;
  padding: 5px;
}
</style>
