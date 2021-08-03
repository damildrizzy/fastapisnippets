<template>
  <div class="px-8">
    <h1 class="mb-4 text-xl font-bold text-gray-700 md:text-2xl">
      Top Authors
    </h1>
    <div
      class="
        flex flex-col
        max-w-sm
        px-6
        py-4
        mx-auto
        bg-white
        rounded-lg
        shadow-md
      "
    >
      <ul class="-mx-4 space-y-6">
        <li
          v-for="author in authors"
          :key="author.id"
          class="flex items-center"
        >
          <img
            src="https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=731&amp;q=80"
            alt="avatar"
            class="object-cover w-10 h-10 mx-4 rounded-full"
          />
          <p>
            <a href="#" class="mx-1 font-bold text-gray-700 hover:underline">{{
              author.full_name
            }}</a
            ><span class="text-sm font-light text-gray-700"
              >{{ author.count }} Snippets Posted</span
            >
          </p>
        </li>
      </ul>
    </div>
  </div>
</template>
;

<script>
import SnippetService from "../services/snippet.service";
export default {
  name: "TopAuthors",
  data() {
    return {
      authors: [],
      message: "",
    };
  },
  mounted() {
    SnippetService.getTopAuthors().then(
      (response) => {
        this.authors = response.data;
      },
      (error) => {
        this.content =
          (error.response &&
            error.response.data &&
            error.response.data.message) ||
          error.message ||
          error.toString();
      }
    );
  },
};
</script>
