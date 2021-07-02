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

      <Form
        @submit="handleLogin"
        :validation-schema="schema"
        class="space-y-5 mt-5"
      >
        <Field
          name="email"
          type="text"
          class="w-full h-12 border border-gray-800 rounded px-3"
          placeholder="Email"
        />
        <ErrorMessage name="email" />
        <div
          class="w-full flex items-center border border-gray-800 rounded px-3"
        >
          <Field
            name="password"
            type="password"
            class="w-4/5 h-12"
            placeholder="password"
          />
          <ErrorMessage name="password" />
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
        .required("required")
        .email("Please Enter a Valid Email Address"),
      password: yup.string().min(8).required("Password is Required"),
    });
    return {
      message: "",
      schema,
    };
  },
  methods: {
    handleLogin(user) {
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
