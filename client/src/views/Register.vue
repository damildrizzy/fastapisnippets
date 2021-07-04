<template>
  <div
    class="
      h-screen
      bg-green-900
      flex flex-col
      space-y-10
      justify-center
      items-center
    "
  >
    <div class="bg-white rounded p-5">
      <h4 class="text-2l font-light">Create Your Account</h4>
      <Form
        @submit="handleRegister"
        :validation-schema="schema"
        class="w-full max-w-lg mt-5"
      >
        <div class="flex flex-wrap -mx-3 mb-6">
          <div class="w-full px-3">
            <label
              class="
                block
                uppercase
                tracking-wide
                float-left
                text-gray-700 text-xs
                font-bold
                mb-2
              "
              for="grid-name"
            >
              Name
            </label>
            <Field
              name="name"
              class="
                appearance-none
                block
                w-full
                bg-gray-200
                text-gray-700
                border border-gray-200
                rounded
                py-3
                px-4
                mb-3
                leading-tight
                focus:outline-none focus:bg-white focus:border-gray-500
              "
              id="grid-name"
              type="text"
              placeholder="Jane Doe"
            ></Field>
          </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
          <div class="w-full px-3">
            <label
              class="
                block
                uppercase
                tracking-wide
                float-left
                text-gray-700 text-xs
                font-bold
                mb-2
              "
              for="grid-username"
            >
              Username
            </label>
            <Field
              name="username"
              class="
                appearance-none
                block
                w-full
                bg-gray-200
                text-gray-700
                border border-gray-200
                rounded
                py-3
                px-4
                mb-3
                leading-tight
                focus:outline-none focus:bg-white focus:border-gray-500
              "
              id="grid-username"
              type="text"
              placeholder="username"
            ></Field>
          </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
          <div class="w-full px-3">
            <label
              class="
                block
                uppercase
                tracking-wide
                float-left
                text-gray-700 text-xs
                font-bold
                mb-2
              "
              for="grid-email"
            >
              Email Address
            </label>
            <Field
              name="email"
              class="
                appearance-none
                block
                w-full
                bg-gray-200
                text-gray-700
                border border-gray-200
                rounded
                py-3
                px-4
                mb-3
                leading-tight
                focus:outline-none focus:bg-white focus:border-gray-500
              "
              id="grid-email"
              type="text"
              placeholder="janedoe@gmail.com"
            ></Field>
          </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
          <div class="w-full px-3">
            <label
              class="
                block
                uppercase
                tracking-wide
                float-left
                text-gray-700 text-xs
                font-bold
                mb-2
              "
              for="grid-password"
            >
              Password
            </label>
            <Field
              name="password"
              class="
                appearance-none
                block
                w-full
                bg-gray-200
                text-gray-700
                border border-gray-200
                rounded
                py-3
                px-4
                mb-3
                leading-tight
                focus:outline-none focus:bg-white focus:border-gray-500
              "
              id="grid-password"
              type="password"
              placeholder="************"
            ></Field>
          </div>
        </div>
        <button
          class="
            text-center
            w-full
            bg-green-400
            rounded-md
            text-white
            py-3
            font-medium
          "
        >
          Create Account
        </button>
      </Form>
    </div>
  </div>
</template>
<script>
import { Form, Field } from "vee-validate";
import * as yup from "yup";

export default {
  name: "Register",
  components: {
    Field,
    Form,
  },
  data: function () {
    const schema = yup.object().shape({
      name: yup.string().required("Name is required"),
      username: yup
        .string()
        .required("Username is required!")
        .min(3, "Must be at least 3 characters!")
        .max(20, "Must be maximum 20 characters!"),
      email: yup
        .string()
        .required("Email is required!")
        .email("Email is invalid!")
        .max(50, "Must be maximum 50 characters!"),
      password: yup
        .string()
        .required("Password is required!")
        .min(6, "Must be at least 6 characters!")
        .max(40, "Must be maximum 40 characters!"),
    });

    return {
      message: "",
      schema,
    };
  },

  methods: {
    handleRegister(user) {
      this.message = "";

      this.$store.dispatch("auth/register", user).then(
        (data) => {
          console.log(data);
        },
        (error) => {
          this.message =
            (error.response &&
              error.response.data &&
              error.response.data.message) ||
            error.message ||
            error.toString();
        }
      );
    },
  },
};
</script>
