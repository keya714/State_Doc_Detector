def last_modified_ts(repo, path):
    try:
        commits = list(repo.iter_commits(paths=path, max_count=1))
        return commits[0].committed_date if commits else 0
    except Exception:
        return 0

def last_change_times(repo_dir, code_paths, doc_paths):
    repo = Repo(repo_dir)
    code_ts = 0
    docs_ts = 0
    for p in code_paths:
        code_ts = max(code_ts, last_modified_ts(repo, p))
    for p in doc_paths:
        docs_ts = max(docs_ts, last_modified_ts(repo, p))
    return code_ts, docs_ts
