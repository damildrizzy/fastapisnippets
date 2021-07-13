<template>
  <div class="px-6 py-8 bg-gray-100">
    <div class="container flex justify-between mx-auto">
      <div class="w-full lg:w-8/12">
        <SnippetList />
      </div>
      <div class="hidden w-4/12 -mx-8 lg:block">
        <TopAuthors />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import SnippetList from "@/components/SnippetList.vue";
import TopAuthors from "@/components/TopAuthors";

export default {
  name: "Home",
  components: {
    SnippetList,
    TopAuthors,
  },
};
</script>
