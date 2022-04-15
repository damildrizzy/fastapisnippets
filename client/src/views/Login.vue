<template>
  <div
      class="
      h-screen
      bg-gray-700
      flex flex-col
      space-y-3
      justify-center
      items-center
    "
  >
    <div
        v-if="message"
        class="
        bg-red-100
        border border-red-400
        text-red-700
        px-4
        rounded
        relative
      "
        role="alert"
    >
      <strong class="font-bold">Error! </strong>
      <span class="block sm:inline">{{ message }}</span>
    </div>
    <div class="bg-white w-96 shadow-xl rounded p-5">
      <h1 class="text-3xl font-light">Welcome</h1>
      <p class="text-sm">Sign in with your email or username</p>

      <Form
          :validation-schema="schema"
          class="space-y-5 mt-5"
          @submit="handleLogin"
      >
        <div>
          <Field
              class="w-full h-12 border border-gray-800 rounded px-3"
              name="identifier"
              placeholder="Email Address or Username"
              type="text"
          />
          <ErrorMessage class="text-red-400 float-left mb-2" name="email"/>
        </div>
        <div>
          <Field
              class="w-full h-12 border border-gray-800 rounded px-3"
              name="password"
              placeholder="password"
              type="password"
          />
          <ErrorMessage class="text-red-400 float-left mb-2" name="password"/>
        </div>

        <button
            class="
            text-center
            w-full
            bg-green-700
            rounded-md
            text-white
            py-3
            font-medium
          "
        >
          Sign In
        </button>
      </Form>
    </div>
    <div>
      <p class="text-gray-300">
        Don't have an account?
        <span class="text-white">
          <router-link to="/register">Create One</router-link>
        </span>
      </p>
    </div>
  </div>
</template>

<script>
import {Form, Field, ErrorMessage} from "vee-validate";
import * as yup from "yup";

export default {
  name: "Login",
  components: {
    Field,
    Form,
    ErrorMessage,
  },
  data() {
    const schema = yup.object().shape({
      identifier: yup
          .string()
          .required("An email address or username is required"),
      password: yup.string().min(6).required("password is required"),
    });
    return {
      message: "",
      schema,
    };
  },
  methods: {
    handleLogin: function (user) {
      this.message = "";

      this.$store.dispatch("auth/login", user).then(
          () => {
            if (this.$route.query.redirect)
              this.$router.push(this.$route.query.redirect);
            else this.$router.push("/");
          },
          (error) => {
            console.log(error.response.data.detail);
            this.message =
                (error.response &&
                    error.response.data &&
                    error.response.data.detail) ||
                error.message ||
                error.toString();
          }
      );
    },
  },
};
</script>
