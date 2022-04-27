import axios from "axios";
import authHeader from "./auth-header";

const API_URL = `${process.env.API_BASE_URL}/snippets`;

class SnippetService {
    getSnippets() {
        return axios.get(API_URL);
    }

    getSnippet(id) {
        return axios.get(`${API_URL}/${id}`);
    }

    createSnippet(snippet) {
        const data = {
            title: snippet.title,
            description: snippet.description,
            code: snippet.code,
            tags: snippet.tags,
        };

        return axios.post(API_URL, data, {headers: authHeader()});
    }

    getTopAuthors() {
        return axios.get(`${API_URL}/top-authors`);
    }
}

export default new SnippetService();
