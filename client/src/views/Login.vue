<template>
  <div
    class="
      h-screen
      bg-white
      flex flex-col
      space-y-10
      justify-center
      items-center
    "
  >
    <div class="bg-white w-96 shadow-xl rounded p-5">
      <h1 class="text-3xl font-light">Welcome</h1>
      <p class="text-sm">Sign in with your email and password</p>

      <form class="space-y-5 mt-5">
        <input
          type="text"
          class="w-full h-12 border border-gray-800 rounded px-3"
          placeholder="Email"
        />
        <div
          class="w-full flex items-center border border-gray-800 rounded px-3"
        >
          <input type="password" class="w-4/5 h-12" placeholder="password" />
          <span class="text-green-500 hover:bg-green-50 rounded-md px-3"
            >Show</span
          >
        </div>

        <button
          class="
            text-center
            w-full
            bg-green-500
            rounded-md
            text-white
            py-3
            font-medium
          "
        >
          Sign In
        </button>
      </form>
    </div>
  </div>
</template>
