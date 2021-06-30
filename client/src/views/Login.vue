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

      <form
        @submit.prevent="handleLogin"
        :validation-schema="schema"
        class="space-y-5 mt-5"
      >
        <input
          type="text"
          class="w-full h-12 border border-gray-800 rounded px-3"
          v-model="email"
          placeholder="Email"
        />
        <div
          class="w-full flex items-center border border-gray-800 rounded px-3"
        >
          <input
            type="password"
            class="w-4/5 h-12"
            v-model="password"
            placeholder="password"
          />
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

<script>
import * as yup from "yup";

export default {
  name: "Login",
  components: {},
  data() {
    const schema = yup.object().shape({
      email: yup.string().required("required"),
      password: yup.string().required("required"),
    });
    return {
      email: "",
      password: "",
      message: "",
      schema,
    };
  },
  methods: {
    handleLogin() {
      this.$store
        .dispatch("auth/login", { email: this.email, password: this.password })
        .then(
          () => {
            console.log(this.$store.state.auth.user);
          },
          (error) => {
            console.log(error);
            this.message = error.toString();
          }
        );
    },
  },
};
</script>
