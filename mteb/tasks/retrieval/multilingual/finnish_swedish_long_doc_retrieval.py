from mteb.abstasks.retrieval import AbsTaskRetrieval
from mteb.abstasks.task_metadata import TaskMetadata

_LANGUAGES = {
    "fin": ["fin-Latn"],
    "swe": ["swe-Latn"],
}


class FinnishSwedishLongDocRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="FinnishSwedishLongDocRetrieval",
        description="Finnish Swedish Long Doc Retrieval (FSLDR) is created by sampling lengthy Finnish and Swedish texts from HPLT v3, selecting high-quality texts, and then using Qwen/Qwen3.5-122B-A10B-GPTQ-Int4 to generate questions based on the texts' paragraphs. We annotated the generated questions and selected only meaningful questions. A dataset item consists of query text pair and associated corpus.",
        reference="https://arxiv.org/abs/2511.09213",
        dataset={
            "path": "akseli-reunamo/FSLDR",
            "revision":"71292584d17c2e28b0481d86553c43fa2a9ea9e6"
        },
        type="Retrieval",
        category="t2t",
        modalities=["text"],
        eval_splits=["dev", "test"],
        eval_langs=_LANGUAGES,
        main_score="ndcg_at_10",
        date=(
            "2011-03-18",
            "2024-12-15",
        ),
        domains=[
            "Web",
        ],  #HPLT v3
        task_subtypes=[],
        license="cc0-1.0",
        annotations_creators="human-annotated",
        dialect=[],
        sample_creation="created",
        bibtex_citation=r"""
@misc{reunamo2025pretrainingfinnishmodernberts,
      title={Pretraining Finnish ModernBERTs}, 
      author={Akseli Reunamo and Laura-Maria Peltonen and Hans Moen and Sampo Pyysalo},
      year={2025},
      eprint={2511.09213},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2511.09213}, 
}
""",
    )
