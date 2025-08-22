from agents import Researcher, Writer, Editor
import time

def run_content_creation_workflow(topic: str):
    """
    Orchestrates the multi-agent content creation workflow.
    """
    print(f"** Orchestrator: Initiating content creation for topic: '{topic}' **\n")

    # Step 1: Researcher agent performs its task
    research_agent = Researcher()
    research_data = research_agent.research(topic)
    print("-" * 50)

    # Step 2: Writer agent uses the research to write a draft
    writer_agent = Writer()
    article_draft = writer_agent.write_draft(topic, research_data)
    print("-" * 50)

    # Step 3: Editor agent polishes the draft
    editor_agent = Editor()
    final_article = editor_agent.edit_article(article_draft)
    print("-" * 50)

    # Display the final output
    print("\n\n** Workflow Complete! Final Output: **")
    print(final_article)

if __name__ == "__main__":
    # Define the topic for the article
    article_topic = "The Future of Artificial Intelligence in Content Creation"
    
    # Run the workflow
    run_content_creation_workflow(article_topic)
