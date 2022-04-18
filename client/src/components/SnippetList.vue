<template>
  <div>
    <div class="flex items-center justify-between">
    <h1 class="text-xl font-bold text-gray-700 md:text-2xl">All Snippets</h1>
  </div>
  <div v-for="snippet in snippets" :key="snippet.id" class="mt-6">
    <div class="max-w-4xl px-5 py-1 mx-auto bg-white shadow-md">
      <div class="mt-2">
        <a class="text-2xl font-bold text-gray-700 hover:underline" href="#">{{
            snippet.title
          }}</a>
        <p class="mt-2 text-gray-600">{{ snippet.description }}</p>
      </div>
      <div class="flex items-center justify-between mt-2">
        <router-link
            :to="{ name: 'snippet-detail', params: { id: snippet.id } }"
            class="text-blue-500 hover:underline"
        >Read more
        </router-link
        >
        <div>
          <a class="flex items-center" href="#"
          ><img
              alt="avatar"
              class="hidden object-cover w-10 h-10 mx-4 rounded-full sm:block"
              src="https://gravatar.com/avatar/dfdceb5f7107bfde6687669026491b89?s=400&d=robohash&r=x"
          />
            <h1 class="font-bold text-gray-700 hover:underline">
              {{ snippet.author.full_name }}
            </h1>
          </a>
        </div>
      </div>
    </div>
  </div>
  </div>

</template>

<script>
import SnippetService from "../services/snippet.service";

export default {
  name: "SnippetList",
  data() {
    return {
      snippets: [],
      message: "",
    };
  },
  mounted() {
    SnippetService.getSnippets().then(
        (response) => {
          this.snippets = response.data;
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
