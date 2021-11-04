<template>
  <div class="px-6 py-8 bg-gray-100">
    <div class="lg:w-9/12">
      <div class="flex items-center justify-between">
        <h1 class="text-xl font-bold text-gray-700 md:text-2xl">
          Post A Snippet
        </h1>
      </div>
      <div class="bg-white rounded p-5 mt-6">
        <Form @submit="handleCreate" class="w-full mt-5">
          <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full px-3">
              <!--              <label-->
              <!--                class="-->
              <!--                  block-->
              <!--                  uppercase-->
              <!--                  tracking-wide-->
              <!--                  float-left-->
              <!--                  text-gray-700 text-xs-->
              <!--                  font-bold-->
              <!--                  mb-2-->
              <!--                "-->
              <!--                for="grid-title"-->
              <!--              >-->
              <!--                Title-->
              <!--              </label>-->
              <Field
                name="title"
                :rules="isRequired"
                class="
                  appearance-none
                  block
                  w-full
                  text-gray-700
                  border border-gray-200
                  rounded
                  py-3
                  px-4
                  mb-3
                  leading-tight
                  focus:outline-none focus:bg-white focus:border-gray-500
                "
                id="grid-title"
                placeholder="Title"
                type="text"
              ></Field>
              <ErrorMessage class="text-red-500" name="title" />
            </div>
          </div>
          <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full px-3">
              <div>
                <!--                <label-->
                <!--                  class="-->
                <!--                    block-->
                <!--                    uppercase-->
                <!--                    tracking-wide-->
                <!--                    text-gray-700 text-xs-->
                <!--                    font-bold-->
                <!--                    mb-2-->
                <!--                  "-->
                <!--                  for="grid-description"-->
                <!--                >-->
                <!--                  Description-->
                <!--                </label>-->
              </div>
              <Field
                as="textarea"
                name="description"
                id="grid-description"
                class="
                  form-textarea
                  appearance-none
                  block
                  w-full
                  text-gray-700
                  border border-gray-200
                  rounded
                  py-3
                  px-4
                  mb-3
                  leading-tight
                  focus:outline-none focus:bg-white focus:border-gray-500
                "
                rows="5"
                placeholder="Description."
                :rules="isRequired"
              ></Field>
              <ErrorMessage class="text-red-500" name="description" />
            </div>
          </div>
          <div class="mb-6">
            <prism-editor
              v-model="code"
              class="my-editor overflow-auto h-96"
              :highlight="highlighter"
              line-numbers
            >
            </prism-editor>

            <ErrorMessage class="text-red-500" name="code" />
          </div>
          <div class="flex flex-wrap -mx-3">
            <div class="w-full px-3">
              <!--              <label-->
              <!--                class="-->
              <!--                  block-->
              <!--                  uppercase-->
              <!--                  tracking-wide-->
              <!--                  float-left-->
              <!--                  text-gray-700 text-xs-->
              <!--                  font-bold-->
              <!--                  mb-2-->
              <!--                "-->
              <!--                for="grid-tags"-->
              <!--              >-->
              <!--                Tags-->
              <!--              </label>-->

              <div id="grid-tags" class="tag-input">
                <div
                  v-for="(tag, index) in tags"
                  :key="tag"
                  class="tag-input__tag"
                >
                  <span @click="removeTag(index)">x</span>
                  {{ tag }}
                </div>
                <input
                  name="tags"
                  type="text"
                  placeholder="Enter a tag"
                  class="tag-input__text"
                  @keyup.enter="addTag"
                  @keyup.space="addTag"
                />
              </div>
            </div>
          </div>
          <button
            class="
              bg-green-500
              hover:bg-green-700
              text-white
              font-bold
              mt-6
              py-2
              px-4
              rounded
            "
          >
            Post Snippet
          </button>
        </Form>
      </div>
    </div>
  </div>
</template>

<script>
import { Form, Field, ErrorMessage } from "vee-validate";
import { PrismEditor } from "vue-prism-editor";
import "vue-prism-editor/dist/prismeditor.min.css";
import SnippetService from "../services/snippet.service";

// import highlighting library (you can use any library you want just return html string)
import { highlight, languages } from "prismjs/components/prism-core";
import "prismjs/components/prism-clike";
import "prismjs/components/prism-javascript";
import "prismjs/components/prism-python";
import "prismjs/themes/prism-tomorrow.css"; // import syntax highlighting styles

export default {
  name: "SnippetCreate",
  components: {
    PrismEditor,
    Field,
    Form,
    ErrorMessage,
  },
  data() {
    return {
      code: "# code snippet goes here",
      tags: [],
    };
  },
  methods: {
    addTag(event) {
      event.preventDefault();
      const val = event.target.value.trim();
      if (val.length > 0) {
        this.tags.push(val);
        event.target.value = "";
      }
    },

    isRequired(value) {
      return value ? true : "*This field is required";
    },

    handleCreate: function (formData) {
      const data = {
        code: this.code,
        tags: this.tags,
      };
      const snippet = JSON.parse(JSON.stringify({ ...formData, ...data }));

      SnippetService.createSnippet(snippet).then(
        (response) => {
          console.log(response.data);
        },
        (error) => {
          console.log(error);
        }
      );
    },

    highlighter() {
      return highlight(this.code, languages.python);
    },

    removeTag(index) {
      this.tags.splice(index, 1);
    },
  },
};
</script>

<style>
/* required class */
.my-editor {
  /* we dont use `language-` classes anymore so that's why we need to add background and text color manually */
  background: #2d2d2d;
  color: #ccc;

  /* you must provide font-family font-size line-height. Example: */
  font-family: Fira code, Fira Mono, Consolas, Menlo, Courier, monospace;
  font-size: 14px;
  line-height: 1.5;
  padding: 5px;
}

.tag-input {
  width: 100%;
  border: 1px solid #eee;
  font-size: 0.9em;
  height: 50px;
  box-sizing: border-box;
  padding: 0 10px;
}

.tag-input__tag {
  height: 30px;
  float: left;
  margin-right: 10px;
  background-color: #eee;
  margin-top: 10px;
  line-height: 30px;
  padding: 0 5px;
  border-radius: 5px;
}

.tag-input__tag > span {
  cursor: pointer;
  opacity: 0.75;
}

.tag-input__text {
  border: none;
  outline: none;
  font-size: 0.9em;
  line-height: 50px;
  background: none;
}
</style>
