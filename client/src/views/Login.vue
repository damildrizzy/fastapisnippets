<template>
  <div
    class="
      h-screen
      bg-gray-200
      flex flex-col
      space-y-10
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
      <p class="text-sm">Sign in with your email and password</p>

      <Form
        @submit="handleLogin"
        :validation-schema="schema"
        class="space-y-5 mt-5"
      >
        <div>
          <Field
            name="email"
            type="text"
            class="w-full h-12 border border-gray-800 rounded px-3"
            placeholder="Email"
          />
          <ErrorMessage name="email" class="text-red-400 float-left mb-2" />
        </div>
        <div>
          <Field
            name="password"
            type="password"
            class="w-full h-12 border border-gray-800 rounded px-3"
            placeholder="password"
          />
          <ErrorMessage name="password" class="text-red-400 float-left mb-2" />
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
  </div>
</template>

<script>
import { Form, Field, ErrorMessage } from "vee-validate";
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
      email: yup
        .string()
        .required("email is required")
        .email("please enter a valid email address"),
      password: yup.string().min(6).required("password is required"),
    });
    return {
      message: "",
      schema,
    };
  },
  methods: {
    handleLogin(user) {
      this.message = "";

      this.$store.dispatch("auth/login", user).then(
        () => {
          console.log(this.$store.state.auth.user);
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
