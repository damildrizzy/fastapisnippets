import axios from "axios";

const API_URL = "http://localhost:8000";

class AuthService {
  login(user) {
    return axios
      .post(`${API_URL}/auth/access-token`, {
        email: user.email,
        password: user.password,
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
