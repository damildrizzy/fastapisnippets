import axios from "axios";
import authHeader from "./auth-header";

const API_URL = "http://localhost:8000/snippets";

class SnippetService {
  getSnippets() {
    return axios.get(API_URL);
  }

  createSnippet(snippet) {
    const data = {
      title: snippet.title,
      description: snippet.description,
      code: snippet.code,
    };

    return axios.post(API_URL, data, { headers: authHeader() });
  }

  getTopAuthors() {
    return axios.get(`${API_URL}/top-authors`);
  }
}

export default new SnippetService();
