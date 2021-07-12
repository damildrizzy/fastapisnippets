<template>
  <div class="flex items-center justify-between">
    <h1 class="text-xl font-bold text-gray-700 md:text-2xl">All Snippets</h1>
    <div>
      <select
        class="
          inline-flex
          justify-center
          w-full
          rounded-md
          border border-gray-300
          shadow-sm
          px-4
          py-2
          bg-white
          text-sm
          font-medium
          text-gray-700
          hover:bg-gray-50
          focus:outline-none
          focus:ring-2
          focus:ring-offset-2
          focus:ring-offset-gray-100
          focus:ring-indigo-500
        "
      >
        <option>Latest</option>
        <option>Highest Rated</option>
      </select>
    </div>
  </div>
  <div class="mt-6">
    <div class="max-w-4xl px-5 py-1 mx-auto bg-white shadow-md">
      <div class="mt-2">
        <a href="#" class="text-2xl font-bold text-gray-700 hover:underline"
          >Build Your New Idea with Laravel Freamwork.</a
        >
        <p class="mt-2 text-gray-600">
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora
          expedita dicta totam aspernatur doloremque. Excepturi iste iusto
        </p>
      </div>
      <div class="flex items-center justify-between mt-2">
        <a href="#" class="text-blue-500 hover:underline">Read more</a>
        <div>
          <a href="#" class="flex items-center"
            ><img
              src="https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=731&amp;q=80"
              alt="avatar"
              class="hidden object-cover w-10 h-10 mx-4 rounded-full sm:block"
            />
            <h1 class="font-bold text-gray-700 hover:underline">Alex John</h1>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SnippetList",
};
</script>
