# Local Deep Researcher

Local Deep Researcher is a fully local web research assistant that uses any LLM hosted by [Ollama](https://ollama.com/search). 

Give it a topic and it will generate a web search query, gather web search results, summarize the results of web search, reflect on the summary to examine knowledge gaps, generate a new search query to address the gaps, and repeat for a user-defined number of cycles. 

It will provide the user a final markdown summary with all sources used to generate the summary

## Install 

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install langchain langchain_community langchain_ollama duckduckgo_search tavily_python
```

## 🚀 Quickstart (after creating a environemnt)

Clone the repository then do a cd:
```shell
cd local-deep-researcher
```

Then edit the `.env` file to customize the environment variables according to your needs. These environment variables control the model selection, search tools, and other configuration settings. When you run the application, these values will be automatically loaded via `python-dotenv` (because `langgraph.json` point to the "env" file).
```shell
cp .env.example .env
```

### Selecting local model with Ollama

1. Download the Ollama app for Mac [here](https://ollama.com/download).

2. Pull a local LLM from [Ollama](https://ollama.com/search). As an [example](https://ollama.com/library/deepseek-r1:8b):
```shell
ollama pull qwen3:latest
```

### Selecting search tool

By default, it will use [DuckDuckGo](https://duckduckgo.com/) for web search, cause it  does not require an API key. 

Optionally, update the `.env` file with the following search tool configuration and API keys. 

If set, these values will take precedence over the defaults set in the `Configuration` class in `configuration.py`. 
```shell
SEARCH_API=xxx # the search API to use, such as `duckduckgo` (default)
MAX_WEB_RESEARCH_LOOPS=xxx # the maximum number of research loop steps, defaults to `3`
FETCH_FULL_PAGE=xxx # fetch the full page content (with `duckduckgo`), defaults to `false`
```


## How it works

Local Deep Researcher is inspired by [IterDRAG](https://arxiv.org/html/2410.04343v1#:~:text=To%20tackle%20this%20issue%2C%20we,used%20to%20generate%20intermediate%20answers.). This approach will decompose a query into sub-queries, retrieve documents for each one, answer the sub-query, and then build on the answer by retrieving docs for the second sub-query. Here, we do similar:
- Given a user-provided topic, use a local LLM (via [Ollama](https://ollama.com/search) or [LMStudio](https://lmstudio.ai/)) to generate a web search query
- Uses a search engine / tool to find relevant sources
- Uses LLM to summarize the findings from web search related to the user-provided research topic
- Then, it uses the LLM to reflect on the summary, identifying knowledge gaps
- It generates a new search query to address the knowledge gaps
- The process repeats, with the summary being iteratively updated with new information from web search
- Runs for a configurable number of iterations (see `configuration` tab)

## Outputs

The output of the graph is a markdown file containing the research summary, with citations to the sources used. All sources gathered during research are saved to the graph state. 

