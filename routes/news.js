import express from 'express';
import axios from 'axios';

const router = express.Router();

// Finance & Loan News API Sources
const NEWS_SOURCES = [
    {
        name: "Marketaux",
        url: "https://api.marketaux.com/v1/news/all",
        params: {
            api_token: "jWPuIqWJHy4GpsU5N1R9PeRGFtVrjRdWKBaoTzVO",
            language: "en",
            sectors: "Financial",
            keywords: "loans,finance,banking",
            limit: 20
        },
        parseResponse: data => data.data.map(article => ({
            title: article.title,
            url: article.url,
            source: article.source,
            pubDate: article.published_at
        }))
    },
    {
        name: "NewsAPI",
        url: "https://newsapi.org/v2/everything",
        params: {
            q: "(loans OR finance OR banking)",
            apiKey: "2e55cdc2-cf05-49bb-b74f-3770c6f35ce1",
            language: "en",
            sortBy: "relevancy",
            pageSize: 20
        },
        parseResponse: data => data.articles.map(article => ({
            title: article.title,
            url: article.url,
            source: article.source.name,
            pubDate: article.publishedAt
        }))
    }
];

// Helper Function: Fetch News Data
const fetchNews = async (source) => {
    try {
        const response = await axios.get(source.url, { params: source.params });
        return source.parseResponse(response.data);
    } catch (error) {
        console.error(`Error fetching from ${source.name}:`, error.message);
        return [];
    }
};

// Route to Get Latest News
router.get('/', async (req, res) => {
    try {
        // Fetch news from all sources concurrently
        const newsResults = await Promise.allSettled(NEWS_SOURCES.map(fetchNews));

        // Process successful responses
        let allNews = newsResults
            .filter(result => result.status === "fulfilled")
            .flatMap(result => result.value)
            .filter(article => article && article.title && article.url); // Remove invalid articles

        // Remove duplicate articles (by URL)
        const uniqueNews = Array.from(new Map(allNews.map(article => [article.url, article])).values());

        return res.json(uniqueNews.length ? uniqueNews : { error: "No news available at the moment" });

    } catch (error) {
        console.error("Error fetching news:", error);
        res.status(500).json({
            error: "Failed to fetch news updates",
            message: error.message || "Internal server error"
        });
    }
});

export default router;
