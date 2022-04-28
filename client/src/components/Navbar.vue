<template>
  <nav
      v-if="!['Login', 'Register'].includes($route.name)"
      class="flex items-center p-6"
  >
    <div class="container flex justify-between mx-auto items-center text-teal">
      <div class="w-full lg:w-6/12">
        <router-link class="font-semibold text-xl tracking-tight" to="/"
        >FastAPI Snippets
        </router-link>
      </div>

      <div class="w-full lg:w-6/12 block flex-grow lg:flex lg:w-auto">
        <div class="text-lg lg:flex-grow text-right">
          <router-link
              class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 mr-4"
              to="/create"
          >
            Create Snippet
          </router-link>
          <div v-if="!loggedIn">
            <router-link
                class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 mr-4"
                to="/login"
            >
              Login
            </router-link>
            <router-link
                class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 mr-4"
                to="/register"
            >Register
            </router-link>
          </div>

        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      loggedIn: this.$store.state.auth.status.loggedIn
    }
  }
};
</script>
