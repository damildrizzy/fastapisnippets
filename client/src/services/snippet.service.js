import axios from "axios";

const API_URL = "http://localhost:8000/snippets";

class SnippetService {
  getSnippets() {
    return axios.get(API_URL);
  }

  getTopAuthors() {
    return axios.get(`${API_URL}/top-authors`);
  }
}

export default new SnippetService();
