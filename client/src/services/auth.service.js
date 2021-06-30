import axios from "axios";

const API_URL = "http://localhost:8000";

class AuthService {
  login(payload) {
    return axios
      .post(`${API_URL}/auth/access-token`, {
        email: payload.email,
        password: payload.password,
      })
      .then((response) => {
        if (response.data.accessToken)
          localStorage.setItem("user", JSON.stringify(response.data));
        return response.data;
      });
  }

  logout() {
    localStorage.removeItem("user");
  }
}

export default new AuthService();
