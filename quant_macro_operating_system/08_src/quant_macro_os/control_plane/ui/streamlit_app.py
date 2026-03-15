from __future__ import annotations

import json
import os
import sys
from datetime import date
from pathlib import Path

SRC_ROOT = Path(__file__).resolve().parents[3]
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

try:
    import streamlit as st
except ModuleNotFoundError:  # pragma: no cover
    class _DummySessionState(dict): pass
    class _DummyContext:
        def __enter__(self): return self
        def __exit__(self, exc_type, exc, tb): return False
    class _DummyStreamlit:
        session_state = _DummySessionState()
        def set_page_config(self, **kwargs): return None
        def title(self, *args, **kwargs): return None
        def caption(self, *args, **kwargs): return None
        def subheader(self, *args, **kwargs): return None
        def image(self, *args, **kwargs): return None
        def markdown(self, *args, **kwargs): return None
        def json(self, *args, **kwargs): return None
        def write(self, *args, **kwargs): return None
        def success(self, *args, **kwargs): return None
        def error(self, *args, **kwargs): return None
        def warning(self, *args, **kwargs): return None
        def dataframe(self, *args, **kwargs): return None
        def text_input(self, label, value="", **kwargs): return value
        def text_area(self, label, value="", **kwargs): return value
        def selectbox(self, label, options, **kwargs): return options[0] if options else None
        def checkbox(self, label, value=False, **kwargs): return value
        def date_input(self, label, value=None, **kwargs): return value
        def button(self, label, **kwargs): return False
        def columns(self, n): return [self for _ in range(n)]
        def metric(self, *args, **kwargs): return None
        def tabs(self, names): return [_DummyContext() for _ in names]
        @property
        def sidebar(self): return _DummyContext()
    st = _DummyStreamlit()

from quant_macro_os.control_plane.api.control_api import ControlAPI
from quant_macro_os.control_plane.services.system_state_service import SystemStateService
from quant_macro_os.control_plane.governance.bootstrap_governance_seed import seed_governance
from quant_macro_os.control_plane.ui.governance_form_guard import registration_readiness


def _resolve_brand_asset(repo_root: Path, filename: str) -> str | None:
    candidates = [
        repo_root / "14_marketing_strategy" / "brand_system_v57_integrated" / filename,
        repo_root / "14_marketing_strategy" / "brand_system_v56_integrated" / filename,
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return None


def _resolve_theme_tokens(repo_root: Path) -> dict:
    theme_file = repo_root / "14_marketing_strategy" / "brand_theme_tokens.json"
    if theme_file.exists():
        return json.loads(theme_file.read_text(encoding="utf-8"))
    return {"palette": {"navy_deep": "#17386D", "blue_primary": "#0B66D6", "ink": "#2E3440", "background": "#F7F8FA", "surface": "#FFFFFF"}}


def _apply_brand_theme(repo_root: Path) -> None:
    palette = _resolve_theme_tokens(repo_root).get("palette", {})
    st.markdown(
        f"""
        <style>
        :root {{
          --eidra-navy: {palette.get("navy_deep", "#17386D")};
          --eidra-blue: {palette.get("blue_primary", "#0B66D6")};
          --eidra-ink: {palette.get("ink", "#2E3440")};
          --eidra-bg: {palette.get("background", "#F7F8FA")};
          --eidra-surface: {palette.get("surface", "#FFFFFF")};
        }}
        .stApp {{ background-color: var(--eidra-bg); color: var(--eidra-ink); }}
        div[data-testid="stSidebar"] {{ background: linear-gradient(180deg, var(--eidra-surface), #eef4fb); }}
        .eidra-banner {{ border: 1px solid rgba(23,56,109,0.12); background: var(--eidra-surface); padding: 0.75rem 1rem; border-radius: 0.9rem; margin-bottom: 1rem; }}
        .eidra-note {{ border-left: 4px solid var(--eidra-blue); padding: 0.65rem 0.9rem; background: rgba(11,102,214,0.05); border-radius: 0.5rem; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def _safe_image(path: str | None, *, width=None):
    if not path:
        return
    try:
        st.image(path, width=width)
    except Exception as exc:  # pragma: no cover
        st.warning(f"brand_asset_unavailable: {exc}")


def _render_brand(repo_root: Path) -> None:
    logo = _resolve_brand_asset(repo_root, "eidra_logo_primary_v56.png")
    monogram = _resolve_brand_asset(repo_root, "eidra_monogram_v56.png")
    _safe_image(logo, width=None)
    st.markdown('<div class="eidra-banner"><strong>EIDRA</strong><br/>Control Plane governado para geração automática de artefatos canônicos.</div>', unsafe_allow_html=True)
    with st.sidebar:
        _safe_image(monogram, width=96)


def _get_api():
    repo_root = Path(st.session_state.get("repo_root", os.getenv("QMOS_REPO_ROOT", str(Path.cwd())))).resolve()
    db_path = Path(st.session_state.get("db_path", os.getenv("QMOS_CONTROL_PLANE_DB", str(Path.cwd().parent / "control_plane.db")))).resolve()
    workdir = Path(st.session_state.get("workdir", os.getenv("QMOS_CONTROL_PLANE_WORKDIR", str(Path.cwd().parent / "qmos_control_plane_workdir")))).resolve()
    return ControlAPI(repo_root=repo_root, db_path=db_path, workdir=workdir)


def _pretty_json(text: str, fallback):
    try:
        return json.loads(text)
    except Exception:
        return fallback


def build_app():
    repo_root = Path(st.session_state.get("repo_root", os.getenv("QMOS_REPO_ROOT", str(Path.cwd())))).resolve()
    favicon = _resolve_brand_asset(repo_root, "eidra_favicon_64_v56.png")
    st.set_page_config(page_title="EIDRA — QMOS Control Plane", page_icon=favicon or "📘", layout="wide")
    _apply_brand_theme(repo_root)
    _render_brand(repo_root)
    st.title("EIDRA — QMOS Control Plane")
    st.caption("Cadastro governado, geração automática de artefatos e execução controlada do pipeline institucional.")

    with st.sidebar:
        st.subheader("Environment")
        st.session_state["repo_root"] = st.text_input("Repository Root", st.session_state.get("repo_root", str(Path.cwd())))
        st.session_state["db_path"] = st.text_input("Control Plane DB", st.session_state.get("db_path", str(Path.cwd().parent / "control_plane.db")))
        st.session_state["workdir"] = st.text_input("Control Plane Workdir", st.session_state.get("workdir", str(Path.cwd().parent / "qmos_control_plane_workdir")))

    api = _get_api()
    system_state = SystemStateService(api.repo_root, api)
    tabs = st.tabs(["Overview", "Projects", "Sources", "Governance", "Knowledge", "Runtime", "Pipelines", "Patch Console", "Audit Ledger"])

    with tabs[0]:
        st.subheader("System State Dashboard")
        snap = system_state.snapshot()
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Tracked Files", snap["tracked_files"])
        c2.metric("Projects", snap["projects"])
        c3.metric("Sources", snap["sources"])
        c4.metric("Pipelines", snap["pipelines"])
        c5, c6, c7 = st.columns(3)
        c5.metric("Pipeline Runs", snap["pipeline_runs"])
        c6.metric("Patches", snap["patches"])
        c7.metric("Audit Events", snap["audit_events"])
        st.json(api.git_status())
        st.markdown('<div class="eidra-note">Primeiro passo em um repositório limpo: clicar em <strong>Seed Governance Defaults</strong>. Depois cadastrar projeto, fonte, governança, pipeline e source instance.</div>', unsafe_allow_html=True)
        if st.button("Seed Governance Defaults"):
            seed_governance()
            st.success("Governance defaults seeded.")

    with tabs[1]:
        st.subheader("Project Registry")
        left, right = st.columns(2)
        with left:
            name = st.text_input("Project Name")
            desc = st.text_area("Project Description")
            owner = st.text_input("Owner", "founder")
            status = st.selectbox("Status", ["active", "draft", "paused"])
            if st.button("Save Project"):
                api.save_project(name, desc, owner, status)
                st.success("Project saved.")
        with right:
            existing_projects = api.list_projects()
            project_names = [row["name"] for row in existing_projects]
            delete_project_name = st.selectbox("Delete Project", [""] + project_names)
            if st.button("Delete Selected Project") and delete_project_name:
                api.delete_project(delete_project_name)
                st.success(f"Project deleted: {delete_project_name}")
        st.dataframe(api.list_projects(), use_container_width=True)

    with tabs[2]:
        st.subheader("Source Registration")
        left, right = st.columns([2,1])

        with left:
            source_name = st.text_input("Source Name", "bcb_sgs")
            source_type = st.selectbox("Source Type", ["api", "manual", "file", "database", "html", "object_storage"])
            source_config = st.text_area("Source Config JSON", value='{"provider":"Banco Central do Brasil","interface":"api","base_url":"https://api.bcb.gov.br/dados/serie/bcdata.sgs","format":"json","category":"macro"}', height=150)
            if st.button("Save Source"):
                api.save_source(source_name, source_type, _pretty_json(source_config, {}))
                st.success("Source saved and artifacts generated.")
        with right:
            source_rows = api.list_sources()
            source_names = [row["name"] for row in source_rows]
            delete_source_name = st.selectbox("Delete Source", [""] + source_names)
            if st.button("Delete Selected Source") and delete_source_name:
                api.delete_source(delete_source_name)
                st.success(f"Source deleted: {delete_source_name}")

        st.dataframe(api.list_sources(), use_container_width=True)

    with tabs[3]:
        st.subheader("Canonical Governance")
        t1, t2, t3, t4, t5, t6 = st.tabs(["Families", "Contracts", "Schedules", "Publish Targets", "Join Policies", "Eligibility"])

        with t1:
            family_name = st.text_input("Family Name", "macro_bcb_series", key="family_name")
            family_desc = st.text_area("Description", "Brazilian macroeconomic time series from BCB SGS", key="family_desc")
            canonical_contract = st.text_input("Canonical Contract", "bcb_sgs_series_v1", key="family_contract")
            grain = st.text_input("Grain", "time_series", key="family_grain")
            owner_vp = st.text_input("Owner VP", "vp_macro_intelligence", key="family_owner")
            family_metadata = st.text_area("Family Metadata JSON", value='{}', height=80, key="family_metadata")
            if st.button("Save Data Family"):
                api.save_data_family(family_name, family_desc, canonical_contract, grain, owner_vp, _pretty_json(family_metadata, {}))
                st.success("Data family saved and artifacts generated.")
            st.dataframe(api.list_data_families(), use_container_width=True)

        with t2:
            contract_name = st.text_input("Contract Name", "bcb_sgs_series_v1", key="contract_name")
            schema_version = st.text_input("Schema Version", "1.0.0", key="schema_version")
            normalized_contract = st.text_area("Normalized Contract JSON", value='{"fields":[{"name":"series_id","type":"string"},{"name":"date","type":"date"},{"name":"value","type":"number"}]}', height=120, key="normalized_contract")
            quality_checks = st.text_area("Quality Checks JSON", value='{"required_fields":["series_id","date","value"]}', height=80, key="quality_checks")
            contract_metadata = st.text_area("Contract Metadata JSON", value='{}', height=80, key="contract_metadata")
            if st.button("Save Contract"):
                api.save_contract(contract_name, schema_version, _pretty_json(normalized_contract, {}), _pretty_json(quality_checks, {}), _pretty_json(contract_metadata, {}))
                st.success("Contract saved and artifacts generated.")
            st.dataframe(api.list_contracts(), use_container_width=True)

        with t3:
            policy_name = st.text_input("Policy Name", "daily_bcb_macro", key="policy_name")
            update_frequency = st.selectbox("Update Frequency", ["daily", "business_daily", "weekly", "monthly", "quarterly", "annual", "event_driven", "on_demand"], key="update_frequency")
            execution_policy = st.text_input("Execution Policy", "run_once_if_fresh", key="execution_policy")
            freshness_sla = st.text_input("Freshness SLA", "24h", key="freshness_sla")
            timezone = st.text_input("Timezone", "America/Sao_Paulo", key="timezone")
            first_eligible_time = st.text_input("First Eligible Time", "08:00", key="first_eligible_time")
            schedule_metadata = st.text_area("Schedule Metadata JSON", value='{}', height=80, key="schedule_metadata")
            if st.button("Save Schedule Policy"):
                api.save_schedule_policy(policy_name, update_frequency, execution_policy, freshness_sla, timezone, first_eligible_time, _pretty_json(schedule_metadata, {}))
                st.success("Schedule policy saved and artifacts generated.")
            st.dataframe(api.list_schedule_policies(), use_container_width=True)

        with t4:
            target_name = st.text_input("Target Name", "macro_bcb_gold", key="target_name")
            layer = st.selectbox("Layer", ["bronze", "silver", "gold", "platinum"], key="target_layer")
            model_name = st.text_input("Model Name", "bcb_macro", key="target_model_name")
            target_desc = st.text_area("Description", "Gold analytical layer for BCB macro series", key="target_desc")
            target_metadata = st.text_area("Target Metadata JSON", value='{}', height=80, key="target_metadata")
            if st.button("Save Publish Target"):
                api.save_publish_target(target_name, layer, model_name, target_desc, _pretty_json(target_metadata, {}))
                st.success("Publish target saved and artifacts generated.")
            st.dataframe(api.list_publish_targets(), use_container_width=True)

        with t5:
            join_policy_name = st.text_input("Join Policy Name", "macro_bcb_join_policy", key="join_policy_name")
            join_data_family = st.text_input("Join Data Family", "macro_bcb_series", key="join_data_family")
            key_columns = st.text_area("Key Columns JSON", value='["series_id"]', height=80, key="key_columns")
            time_key = st.text_input("Time Key", "date", key="time_key")
            alignment_policy = st.text_input("Alignment Policy", "left_latest_available", key="alignment_policy")
            join_metadata = st.text_area("Join Metadata JSON", value='{}', height=80, key="join_metadata")
            if st.button("Save Join Key Policy"):
                api.save_join_key_policy(join_policy_name, join_data_family, _pretty_json(key_columns, []), time_key, alignment_policy, _pretty_json(join_metadata, {}))
                st.success("Join policy saved and artifacts generated.")
            st.dataframe(api.list_join_key_policies(), use_container_width=True)

        with t6:
            freq = st.selectbox("Frequency", ["daily", "business_daily", "weekly", "monthly", "quarterly", "annual", "event_driven", "on_demand"], key="eligibility_freq")
            selected_date = st.date_input("Date", value=date.today(), key="eligibility_date")
            st.write({"should_run": api.evaluate_schedule(freq, selected_date.year, selected_date.month, selected_date.day)})

    with tabs[4]:
        st.subheader("Knowledge Asset Registration")
        asset_name = st.text_input("Knowledge Asset Name", "berkeley_macro_paper")
        domain = st.selectbox("Knowledge Domain", ["macro_economics", "quantitative_finance", "statistics", "econometrics", "machine_learning", "data_engineering", "market_microstructure", "portfolio_theory", "risk_management", "signal_processing"])
        asset_type = st.selectbox("Asset Type", ["paper", "book", "dataset", "note", "canon", "playbook"])
        location_hint = st.text_input("Location Hint", "12_docs/knowledge_pillars/literature_repository/macro_economics")
        tags = st.text_area("Tags JSON", value='["macro","research"]', height=80)
        summary = st.text_area("Summary", value="Institutional knowledge asset registered from the control plane.", height=100)
        asset_metadata = st.text_area("Knowledge Metadata JSON", value='{}', height=80)
        if st.button("Save Knowledge Asset"):
            result = api.save_knowledge_asset(asset_name, domain, asset_type, location_hint, _pretty_json(tags, []), summary, _pretty_json(asset_metadata, {}))
            st.json(result)
            st.success("Knowledge asset saved and artifacts generated.")
        st.dataframe(api.list_knowledge_assets(), use_container_width=True)

    with tabs[5]:
        st.subheader("Runtime Planning and E2E")
        source_names = [row["name"] for row in api.list_sources()]
        data_families = [row["family_name"] for row in api.list_data_families()]
        contracts = [row["contract_name"] for row in api.list_contracts()]
        schedules = [row["policy_name"] for row in api.list_schedule_policies()]
        publish_targets = [row["target_name"] for row in api.list_publish_targets()]
        join_policies = [row["policy_name"] for row in api.list_join_key_policies()]
        pipelines = [row["name"] for row in api.list_pipelines()]
        readiness = registration_readiness(source_names, data_families, contracts, schedules, publish_targets, join_policies, pipelines)
        if not readiness["ready"]:
            st.write({"governance_blocked": True, "missing": readiness["missing"]})

        instance_name = st.text_input("Instance Name", "bcb_sgs_daily_instance")
        source_name = st.selectbox("Source Name", source_names) if source_names else None
        data_family = st.selectbox("Data Family", data_families) if data_families else None
        canonical_contract_name = st.selectbox("Contract", contracts) if contracts else None
        schedule_policy_name = st.selectbox("Schedule Policy", schedules) if schedules else None
        publish_target_name = st.selectbox("Publish Target", publish_targets) if publish_targets else None
        join_key_policy_name = st.selectbox("Join Policy", join_policies) if join_policies else None
        pipeline_name = st.selectbox("Pipeline", pipelines) if pipelines else None
        is_enabled = st.checkbox("Enabled", value=True)
        metadata_json = st.text_area("Instance Metadata JSON", value='{}', height=100)
        if st.button("Save Source Instance"):
            if not readiness["ready"]:
                st.write({"status": "blocked", "reason": "missing_governance_dependencies", "missing": readiness["missing"]})
            else:
                api.save_source_instance(instance_name, source_name, source_name, data_family, canonical_contract_name, schedule_policy_name, publish_target_name, join_key_policy_name, pipeline_name, is_enabled, _pretty_json(metadata_json, {}))
                st.success("Source instance saved and artifacts generated.")
        st.dataframe(api.list_source_instances(), use_container_width=True)

        plan_date = st.date_input("Plan Date", value=date.today(), key="plan_date")
        if st.button("Generate Runtime Plan"):
            st.json(api.runtime_plan_for_date(plan_date.year, plan_date.month, plan_date.day))
        instance_options = [row["instance_name"] for row in api.list_source_instances()]
        e2e_instance = st.selectbox("E2E Source Instance", instance_options) if instance_options else None
        if st.button("Run Source Instance E2E") and e2e_instance:
            st.json(api.run_source_instance_e2e(e2e_instance, plan_date.year, plan_date.month, plan_date.day))
        st.markdown("### Published Artifacts")
        st.dataframe(api.list_publish_artifacts(), use_container_width=True)

    with tabs[6]:
        st.subheader("Pipeline Execution Dashboard")
        presets = api.get_pipeline_presets()
        preset_name = st.selectbox("Pipeline Preset", list(presets.keys()))
        preset_alias = st.text_input("Preset Alias", preset_name)
        if st.button("Create Pipeline from Preset"):
            st.json(api.create_pipeline_from_preset(preset_name, preset_alias))

        pipeline_name = st.text_input("Pipeline Name", "bcb_sgs_ingestion")
        source_names = [row["name"] for row in api.list_sources()]
        pipeline_source_name = st.selectbox("Pipeline Source", source_names) if source_names else None
        steps = st.text_area("Steps JSON", value='["source","ingest","normalize","validate","publish"]', height=100)
        if st.button("Save Pipeline") and pipeline_source_name:
            api.save_pipeline(pipeline_name, pipeline_source_name, _pretty_json(steps, []))
            st.success("Pipeline saved and artifacts generated.")

        st.dataframe(api.list_pipelines(), use_container_width=True)
        pipeline_options = [row["name"] for row in api.list_pipelines()]
        pipeline_to_run = st.selectbox("Pipeline to Run", pipeline_options) if pipeline_options else None
        runtime = st.text_area("Runtime Params JSON", value="{}", height=120)
        if st.button("Run Pipeline") and pipeline_to_run:
            st.json(api.run_pipeline(pipeline_to_run, _pretty_json(runtime, {})))
        st.dataframe(api.list_pipeline_runs(), use_container_width=True)

    with tabs[7]:
        st.subheader("Patch Governance Dashboard")
        files = api.list_files()
        target = st.selectbox("Target File", files, index=0 if files else None)
        current = api.read_file(target) if target else ""
        st.text_area("Current Content", current, height=220)
        proposed = st.text_area("Proposed Content", current, height=220)
        approver = st.text_input("Approver", "founder")
        if st.button("Preview Diff") and target:
            st.session_state["cp_diff"] = api.preview_diff(target, proposed)
        if st.button("Validate Patch") and target:
            st.session_state["cp_validation"] = api.validate_patch(target, proposed)
        if st.button("Stage Patch") and target:
            pid = api.stage_patch(target, proposed)
            st.session_state["cp_patch_id"] = pid
            st.success(f"Patch staged: {pid}")
        if st.button("Approve Patch"):
            pid = st.session_state.get("cp_patch_id")
            if pid:
                api.approve_patch(int(pid), approver)
                st.success(f"Patch approved: {pid}")
        st.text_area("Validation Result", st.session_state.get("cp_validation", ""), height=80)
        st.text_area("Unified Diff", st.session_state.get("cp_diff", ""), height=300)
        st.dataframe(api.list_patches(), use_container_width=True)

    with tabs[8]:
        st.subheader("Audit Ledger")
        st.dataframe(api.get_audit_events()[:1000], use_container_width=True)

if __name__ == "__main__":
    build_app()
