{{- define "app-template.releasename" -}}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{- define "app-template.imagedetails" -}}
imagename: {{ .Values.app.repoName }}/{{ .Values.app.imageName }}:latest
{{- end -}}