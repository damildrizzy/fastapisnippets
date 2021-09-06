<template>
  <div class="px-6 py-8 bg-gray-100">
    <div class="lg:w-9/12">
      <div class="flex items-center justify-between">
    <h1 class="text-xl font-bold text-gray-700 md:text-2xl">Post A Snippet</h1>
    </div>
    <div class="bg-white rounded p-5 mt-6">
      <Form class="w-full mt-5">
        <div class="flex flex-wrap -mx-3 mb-6">
          <div class="w-full px-3">
            <label
              class="
                block
                uppercase
                tracking-wide
                float-left
                text-gray-700 text-xs
                font-bold
                mb-2
              "
              for="grid-title"
            >
              Title
            </label>
            <Field
              name="title"
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
              type="text"
            ></Field>
          </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
          <div class="w-full px-3">
            <div>
                <label
                class="
                  block
                  uppercase
                  tracking-wide
                  text-gray-700 text-xs
                  font-bold
                  mb-2
                "
                for="grid-description"
              >
                Description
              </label>
            </div>
           <vue-editor v-model="description" id="grid-description"></vue-editor>  
          </div>
        </div>
        
        <div>
          <prism-editor
          class="my-editor overflow-auto h-96"
          v-model="code"
          :highlight="highlighter"
          line-numbers>
        </prism-editor>
        </div>
        
      </Form>
      
    </div>
    </div>
    
  </div>
</template>

<script>
import { Form, Field } from "vee-validate";
import { PrismEditor } from "vue-prism-editor";
import { VueEditor } from "vue3-editor";
import "vue-prism-editor/dist/prismeditor.min.css"; // import the styles somewhere

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
    VueEditor,
    Field,
    Form,
  },
  data() {
    return {
      code: "# code snippet goes here",
      description: ""
    };
  },
  methods: {
    highlighter() {
      return highlight(this.code, languages.python);
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

/* optional class for removing the outline */
.prism-editor__textarea:focus {
  outline: none;
}
</style>
