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
              alt="avatar"
              class="object-cover w-10 h-10 mx-4 rounded-full"
              src="https://gravatar.com/avatar/dfdceb5f7107bfde6687669026491b89?s=400&d=robohash&r=x"
          />
          <p>
            <a class="mx-1 font-bold text-gray-700 hover:underline" href="#">{{
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
