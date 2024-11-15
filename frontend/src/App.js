import React, { useState } from "react";
import SearchBar from "./components/SearchBar";
import NewsList from "./components/NewsList";

function App() {
  const [articles, setArticles] = useState([]);

  const fetchNews = async (query) => {
    try {
      const response = await fetch(`/api/news?query=${query}`);
      const data = await response.json();
      if (data.articles) {
        setArticles(data.articles);
      } else {
        console.error("No articles found");
      }
    } catch (error) {
      console.error("Error fetching news:", error);
    }
  };

  return (
    <div>
      <h1>News Feed Aggregator</h1>
      <SearchBar onSearch={fetchNews} />
      <NewsList articles={articles} />
    </div>
  );
}

export default App;
